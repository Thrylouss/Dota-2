import re, requests, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .models import Attribute, Hero, Role, HeroRoles, Aspects, Skills


def process_value(request_values, item_value=None):
    if item_value is None:
        item_value = {}
    response_values = ''
    for index_value, value in enumerate(request_values):
        if index_value > 0:
            response_values += '/'
        if item_value.get('is_percentage', False):
            if '%' not in str(value):
                response_values += f'{value}%'
            else:
                response_values += str(value)
        else:
            response_values += str(value)
    return response_values


def process_special_values(description, ability_, is_shard_=None, ):
    values = []

    for special_value in ability_.get('special_values', []):
        shard_scepter = f'{"values_shard" if is_shard_ == 'True' else "values_scepter"}'
        if is_shard_ is None:
            values.append({
                'value': str(special_value['values_float'][0]) if special_value.get('values_float') else '0',
                'name': special_value['name']
            })

        elif is_shard_ == 'facet':
            value = special_value['facet_bonus']['values']
            if value:
                values.append({
                    'value': str(value[0]),
                    'name': special_value['name']
                })

        elif special_value.get(shard_scepter):
            values.append({
                'value': str(special_value[shard_scepter][0]),
                'name': special_value['name']
            })

    for param in values:
        pattern = r'%{}%'.format(re.escape(param['name']))
        description = re.sub(pattern, param['value'], description)

        percentage_pattern = r'%{}%'.format(re.escape(param['name']))
        description = re.sub(percentage_pattern, param['value'], description)

        bonus_pattern = r'%bonus_{}%'.format(re.escape(param['name']))
        description = re.sub(bonus_pattern, param['value'], description)
    description = re.sub(r'%%', '%', description)
    return description


def get_hero_info():
    start_time = time.time()  # 51:33 my time
    len_heroes = len(
        requests.get(f'https://www.dota2.com/datafeed/herolist?language=english').json().get('result').get('data').get(
            'heroes'))
    hero_id = 0  # default 0
    heroes_count = 0
    # heroes = [] # не использовать, он выводит данные о герое для теста
    while heroes_count != len_heroes:
        hero_id += 1
        print(hero_id)
        response = requests.get(f'https://www.dota2.com/datafeed/herodata?language=english&hero_id={hero_id}')
        data = response.json().get('result').get('data').get('heroes')
        if not data or hero_id == 127:
            continue
        hero = data[0]
        abilities = []
        facets = []

        hero_data = {
            'agi_base': hero.get('agi_base'),
            'agi_gain': hero.get('agi_gain'),
            'armor': hero.get('armor'),
            'attack_range': hero.get('attack_range'),
            'attack_rate': hero.get('attack_rate'),
            'damage_max': hero.get('damage_max'),
            'damage_min': hero.get('damage_min'),
            'difficulty': hero.get('complexity'),
            'history': hero.get('bio_loc'),
            'health_regen': hero.get('health_regen'),
            'description': hero.get('hype_loc'),
            'int_base': hero.get('int_base'),
            'int_gain': hero.get('int_gain'),
            'magic_resistance': hero.get('magic_resistance'),
            'mana_regen': hero.get('mana_regen'),
            'max_health': hero.get('max_health'),
            'max_mana': hero.get('max_mana'),
            'movement_speed': hero.get('movement_speed'),
            'name': hero.get('name'),
            'name_loc': hero.get('name_loc'),
            'primary_attr': hero.get('primary_attr'),
            'projectile_speed': hero.get('projectile_speed'),
            'str_base': hero.get('str_base'),
            'str_gain': hero.get('str_gain'),
            'turn_rate': hero.get('turn_rate'),
            "role_levels": hero.get('role_levels'),
            'advice': hero.get('npe_desc_loc'),
            'attack_type': hero.get('attack_capability'),  # 1,2
            'sight_range_day': hero.get('sight_range_day'),
            'sight_range_night': hero.get('sight_range_night'),
        }

        def process_ability(ability_, is_scepter=False, is_shard=False, is_facet=False):
            ability_data = {
                'is_innate': ability_.get('ability_is_innate'),
                'name': ability_.get('name_loc'),
                'description': process_special_values(ability_.get('desc_loc'), ability_),
                'tip': ability_.get('lore_loc'),
                'cast_ranges': ability_.get('cast_ranges'),
                'durations': ability_.get('durations'),
                'cooldowns': ability_.get('cooldowns'),
                'mana_cost': ability_.get('mana_costs'),
                'damages': ability_.get('damages'),
                'target_team': ability_.get('target_team'),
                'target_type': ability_.get('target_type'),
                'immunity': ability_.get('immunity'),
                'dispellable': ability_.get('dispellable'),
                'damage_type': ability_.get('damage'),
                'behavior': ability_.get('behavior'),
                'scepter_description': '',
                'shard_description': '',
                'aghs_icon':'',
                'is_facet': is_facet
                }

            hero_name_loc = hero.get('name_loc')
            hero_name = ''
            for char_ in hero_name_loc:
                if char_ == ' ':
                    hero_name += '_'
                elif char_ == '-':
                    continue
                else:
                    hero_name += char_.lower()
            if ability_.get('ability_has_scepter') or ability_.get('ability_is_granted_by_scepter'):
                video_skill_tag = f'{hero_name}_aghanims_scepter'
            elif ability_.get('ability_is_granted_by_shard') or ability_.get('ability_has_shard'):
                video_skill_tag = f'{hero_name}_aghanims_shard'
            else:
                video_skill_tag = ability_.get('name')
            ability_data[
                'video'] = (f'https://cdn.akamai.steamstatic.com/apps/dota2/videos/dota_react/abilities/'
                            f'{hero_name}/{video_skill_tag}.mp4')
            if is_scepter:
                scepter_loc = ability_.get('scepter_loc')
                ability_data['scepter_description'] = process_special_values(scepter_loc, ability_, 'False')
            if is_shard:
                shard_loc = ability_.get('shard_loc')
                ability_data['shard_description'] = process_special_values(shard_loc, ability_, 'True')
            ability_data['ability_is_granted_by_shard'] = ability_.get('ability_is_granted_by_shard')
            ability_data['ability_is_granted_by_scepter'] = ability_.get('ability_is_granted_by_scepter')
            ability_data['ability_has_scepter'] = ability_.get('ability_has_scepter')
            ability_data['ability_has_shard'] = ability_.get('ability_has_shard')
            # Обработка специальных значений
            special_values = []
            for special_value_ in ability_.get('special_values'):
                if special_value_.get('heading_loc'):
                    special_values.append({
                        'heading_loc': special_value_.get('heading_loc'),
                        'values_float': special_value_.get('values_float'),
                        'is_percentage': special_value_.get('is_percentage')
                    })
            ability_data['special_values'] = special_values
            ability_icon_base_url = "https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react"
            if ability.get('ability_is_innate'):
                ability_icon = f"{ability_icon_base_url}/icons/innate_icon.png"
            else:
                ability_icon = f"{ability_icon_base_url}/abilities/{ability.get('name')}.png"
            aghs_icon = ''
            if ability_data.get('scepter_description') or ability_data.get('ability_is_granted_by_scepter'):
                aghs_icon = f"{ability_icon_base_url}/heroes/stats/aghs_scepter.png"
            elif ability_data.get('shard_description') or ability_data.get('ability_is_granted_by_shard'):
                aghs_icon = f"{ability_icon_base_url}/heroes/stats/aghs_shard.png"
            ability_data['icon'] = ability_icon
            ability_data['aghs_icon'] = aghs_icon


            return ability_data

        def process_ability_status(ability_,is_facet=False):
            if is_facet:
                abilities.append(process_ability(ability_, is_facet=True))
                return
            if (ability_.get('ability_has_scepter') or ability_.get('ability_is_granted_by_scepter')) and ability_.get('scepter_loc'):
                abilities.append(process_ability(ability_, is_scepter=True))
                if ability_.get('ability_has_scepter') and not ability_.get('ability_is_granted_by_scepter'):
                    abilities.append(process_ability(ability_))
            elif (ability_.get('ability_is_granted_by_shard') or ability_.get('ability_has_shard')) and ability_.get('shard_loc'):
                abilities.append(process_ability(ability_, is_shard=True))
                if ability_.get('ability_has_shard') and not ability_.get('ability_is_granted_by_shard'):
                    abilities.append(process_ability(ability_))
            else:
                abilities.append(process_ability(ability_))

        for facet_ability in hero.get('facet_abilities'):
            for ability in facet_ability.get('abilities'):
                if ability:
                    process_ability_status(ability,is_facet=True)
        for ability in hero.get('abilities'):
            process_ability_status(ability)
        name_hero_loc = hero.get('name_loc')
        name_hero = ''
        for char in name_hero_loc:
            if char == ' ':
                continue
            else:
                name_hero += char.lower()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        def load_page():
            retire = 10
            for attempt in range(retire):
                try:
                    driver.set_page_load_timeout(20)
                    driver.get(f'https://www.dota2.com/hero/{name_hero}?l=english')
                    time.sleep(5)
                    html = driver.page_source
                    soup_ = BeautifulSoup(html, 'html.parser')
                    if soup_.find('video', class_="_22nJ5nsfHDS2jEscPEne0-"):
                        return soup_
                    raise TimeoutException
                except TimeoutException:
                    print(f"Timeout: Страница не загрузилась, перезагрузка (попытка {attempt + 1}/{retire})")
                    driver.refresh()
            print('cant load page')

        soup = load_page()
        video_tag = soup.find('video', class_="_22nJ5nsfHDS2jEscPEne0-")
        hero_data['hero_video_src'] = video_tag.find('source', {'type': 'video/webm'}).get('src')
        hero_data['hero_image_src'] = video_tag.find('img').get('src')
        hero_name = hero.get('name')
        name_hero_icon = hero_name[len("npc_dota_hero_"):]
        hero_data['hero_icon_src'] = f'https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/heroes/{name_hero_icon}.png'
        talents = [div.text for div in soup.find_all('div', class_="_1SJ4JZrp7rwc6FG-vINkFn")[:8]]
        facets_skills = []
        facets_big_div = soup.find_all('div', class_="swTQdhtrGo5VPAWX79ypS")
        for facet_big_div in facets_big_div:
            facet_big_div_value = facet_big_div.find('div', class_="_1pbjBspjgUjS0B46DY5KJP")
            facets_skills.append(facet_big_div_value.find('div',
                                                          class_="_1rBGHCdy0eU5X2K5p3xSVY").text
                                 if facet_big_div_value else facet_big_div_value)
        facets_data = hero.get('facets')
        count = 0
        for facet_data in facets_data:
            add = False
            facet_abilities = []
            for facet_ability in hero.get('facet_abilities'):
                if facet_ability.get('abilities'):
                    facet_abilities.append(facet_ability.get('abilities')[0])
            lists = [hero.get('abilities'), facet_abilities]
            for item in lists:
                for ability in item:
                    def draw_facet():
                        ability_desc = ability.get('facets_loc')
                        ability_desc = ability_desc[0] if ability_desc[0] else ability_desc[1]
                        ability_desc = process_special_values(ability_desc, ability, 'facet')
                        ability_name = ability['name_loc']
                        ability_icon = "https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react"
                        if ability.get('ability_is_innate'):
                            ability_icon = f"{ability_icon}/icons/innate_icon.png"
                        else:
                            ability_icon = f"{ability_icon}/abilities/{ability.get('name')}.png"
                        facets.append({
                            'title': facet_data.get('title_loc'),
                            'description': facet_data.get('description_loc'),
                            'icon': f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/icons/facets/"
                                    f"{facet_data.get('icon')}.png",
                            'ability_description': ability_desc,
                            'ability_name': ability_name,
                            'ability_icon': ability_icon,
                            'full_description': None
                        })

                    if len(facets_skills) == 2:
                        if ability.get('name_loc') == facets_skills[count]:
                            draw_facet()
                            add = True
                    elif len(facets_skills) == 1:
                        if ability.get('name_loc') == facets_skills[0]:
                            draw_facet()
                            add = True
            if not add:
                facets_full_description = soup.find('div', class_="_2tOvRyMjowK6qLedqmX1Hg").text \
                    if soup.find('div', class_="_2tOvRyMjowK6qLedqmX1Hg") else None
                facets.append({
                    'title': facet_data.get('title_loc'),
                    'description': facet_data.get('description_loc'),
                    'icon': f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/icons/facets/"
                            f"{facet_data.get('icon')}.png",
                    'ability_description': None,
                    'ability_name': None,
                    'ability_icon': None,
                    'full_description': facets_full_description
                })
            count += 1
        driver.quit()
        new_hero = Hero(
            icon=hero_data['hero_icon_src'],
            name=hero_data['name_loc'],
            main_attribute=Attribute.objects.get(id=hero_data['primary_attr'] + 1),
            complexity=hero_data['difficulty'],
            advice=hero_data['advice'],
            history=hero_data['history'],
            attack={
                'attack_rate': hero_data['attack_rate'],
                'attack_range': hero_data['attack_range'],
                'projectile_speed': hero_data['projectile_speed'],
                'damage': f'{hero_data["damage_min"]} - {hero_data["damage_max"]}'
            },
            defense={
                'armor': hero_data['armor'],
                'magic_resistance': hero_data['magic_resistance']
            },
            mobility={
                'movement_speed': hero_data['movement_speed'],
                'visibly': f'{hero_data["sight_range_day"]}/{hero_data["sight_range_night"]}',
                'turn_rate': hero_data['turn_rate']
            },
            hp={
                'health': hero_data['max_health'],
                'health_regen': hero_data['health_regen']
            },
            mp={
                'mana': hero_data['max_mana'],
                'mana_regen': hero_data['mana_regen']
            },
            attributes={
                'agi_base': hero_data['agi_base'],
                'int_base': hero_data['int_base'],
                'str_base': hero_data['str_base'],
                'agi_gain': hero_data['agi_gain'],
                'int_gain': hero_data['int_gain'],
                'str_gain': hero_data['str_gain']
            },
            attack_type='melee' if hero_data['attack_type'] == 1 else 'ranged',
            talents={
                'talent_1': talents[0],
                'talent_2': talents[1],
                'talent_3': talents[2],
                'talent_4': talents[3],
                'talent_5': talents[4],
                'talent_6': talents[5],
                'talent_7': talents[6],
                'talent_8': talents[7]
            },
            description=hero_data['description'],
            video=hero_data['hero_video_src'],
            image=hero_data['hero_image_src']
        )
        new_hero.save()
        for index, ability in enumerate(abilities):
            new_skill = Skills(
                name=ability['name'],
                icon=ability['icon'],
                description=ability['description'],
                hero=new_hero,
                number=index,
                tip=ability['tip'],
                cooldown=process_value(ability['cooldowns']),
                mana_cost=process_value(ability['mana_cost']),
                video=ability['video'],
                is_innate=ability['is_innate'],
                ability_is_granted_by_shard=ability['ability_is_granted_by_shard'],
                ability_is_granted_by_scepter=ability['ability_is_granted_by_scepter'],
                ability_has_scepter=ability['ability_has_scepter'],
                ability_has_shard=ability['ability_has_shard'],
                scepter_description=ability['scepter_description'],
                shard_description=ability['shard_description'],
                aghs_icon=ability['aghs_icon'],
                is_facet=ability['is_facet']
            )
            spell_immunity = int(ability.get('immunity'))
            if spell_immunity == 3 or spell_immunity == 1:
                spell_immunity = 'yes'
            elif spell_immunity == 2 or spell_immunity == 4:
                spell_immunity = 'no'
            elif spell_immunity == 0:
                spell_immunity = None
            elif spell_immunity == 5:
                spell_immunity = 'only friends'
            dispellable = int(ability.get('dispellable'))
            if dispellable == 3 or dispellable == 1:
                dispellable = 'no'
            elif dispellable == 4 or dispellable == 2:
                dispellable = 'yes'
            elif dispellable == 0:
                dispellable = None
            elif dispellable == 1:
                dispellable = 'Only Strong Dispels'

            target_type = int(ability.get('target_type'))
            if ability.get('target_team') == 1:
                if (target_type & 7) == 7:
                    affects = "allied units and buildings"
                elif (target_type & 3) == 3:
                    affects = "allied units"
                elif (target_type & 5) == 5:
                    affects = "allied heroes and buildings"
                elif (target_type & 1) == 1:
                    affects = "allied heroes"
                elif (target_type & 2) == 2:
                    affects = "allied creeps"
                else:
                    affects = "allies"
            elif ability.get('target_team') == 2:
                if (target_type & 7) == 7:
                    affects = "enemy units and buildings"
                elif (target_type & 3) == 3:
                    affects = "enemy units"
                elif (target_type & 5) == 5:
                    affects = "enemy heroes and buildings"
                elif (target_type & 1) == 1:
                    affects = "enemy heroes"
                elif (target_type & 2) == 2:
                    affects = "enemy creeps"
                else:
                    affects = "enemies"
            elif ability.get('target_team') == 3:
                if (target_type & 1) == 1:
                    affects = "heroes"
                else:
                    affects = "units"
            else:
                affects = None
            behavior = int(ability.get('behavior'))
            if behavior & 65536:
                target = "aura"
            elif behavior & 4:
                target = "no target"
            elif behavior & 8:
                target = "unit target"
            elif behavior & 16:
                target = "point target"
            elif behavior & 32:
                target = "point aoe"
            elif behavior & 128:
                target = "channeled"
            elif behavior & 512:
                target = "toggle"
            elif behavior & 4096:
                target = "autocast"
            elif behavior & 2:
                target = "passive"
            else:
                target = None
            skill_spell_effects = {'PIERCES_SPELL_IMMUNITY': spell_immunity, 'DISPELLABLE': dispellable,
                                   'AFFECTS': affects, 'ABILITY': target}
            for special_value in ability['special_values']:
                values_float = special_value['values_float']
                values = process_value(values_float, special_value)
                skill_spell_effects[special_value['heading_loc']] = values
                skill_spell_effects['CAST_RANGE'] = '/'.join(map(str, ability.get('cast_ranges')))
            skill_spell_effects['DURATION'] = '/'.join(map(str, ability.get('durations')))
            new_skill.spell_effects = skill_spell_effects
            if ability['damage_type'] == 4:
                damage_type = 'pure'
            elif ability['damage_type'] == 2:
                damage_type = 'magical'
            elif ability['damage_type'] == 1:
                damage_type = 'physical'
            else:
                damage_type = None
            new_skill.damage_type = damage_type
            new_skill.save()
        for aspect in facets:
            Aspects.objects.create(
                title=aspect['title'],
                description=aspect['description'],
                icon=aspect['icon'],
                ability_description=aspect['ability_description'],
                ability_name=aspect['ability_name'],
                ability_icon=aspect['ability_icon'],
                full_description=aspect['full_description'],
                hero=new_hero
            )
        for index, role in enumerate(hero_data['role_levels']):
            id_ = index + 1
            role_bd = Role.objects.get(id=id_)
            HeroRoles.objects.create(
                hero=new_hero,
                level=role,
                role=role_bd
            )
        heroes_count += 1
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.6f} секунд")
    return 'ok'
