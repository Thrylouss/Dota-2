import {useParams} from "react-router-dom";
import {GetCurrentHero} from "../../features/GetCurrentHero/GetCurrentHero.jsx";
import './current-hero.css'
import HeroVideo from "./Hero_video.jsx";
import HeroAttr from "./Hero_attr.jsx";
import HeroType from "./Hero_type.jsx";
import talents from '../../../public/talents.svg'
import {GetCurrentHeroSkills} from "../../features/GetCurrentHeroSkills/GetCurrentHeroSkills.jsx";
import HeroSkills from "./Hero_skills.jsx";
import HeroAbout from "./Hero_about.jsx";
import CurrentHeroAspects from "../CurrentHeroAspects/Current_hero_aspects.jsx";
import CurrentHeroSkillsVideo from "../CurrentHeroSkills/Current_hero_skills_video.jsx";
import CurrentHeroTalents from "../CurrentHeroTalents/CurrentHeroTalents.jsx";
import {useEffect, useState} from "react";
import allHeroes from '../../../public/pppp.bmp'
import {PrevHero} from "../nextPrevHeroes/prevHero.jsx";
import {NextHero} from "../nextPrevHeroes/nextHero.jsx";
import HeroesList from "../Heroes/Heroes-list.jsx";
import axios from "axios";
export default function CurrentHero() {
    const {name} = useParams()
    const hero = GetCurrentHero(name).heroes
    const [nextHero, setNextHero] = useState({})
    const [prevHero, setPrevHero] = useState({})
    useEffect(()=> {
        const fetchHeroes = async () => {
            try {
                await axios.get('http://localhost:8000/api/v1/heroes-list/')
                    .then(res => {
                        const heroes = res.data.sort((a, b) => a.name > b.name ? 1 : -1)
                        heroes.find(hero => {
                            if (hero.name === name) {
                                setNextHero(heroes[heroes.indexOf(hero) + 1])
                                setPrevHero(heroes[heroes.indexOf(hero) - 1])
                            }
                        })
                    })
            }
            catch (e) {
                console.log(e)
            }
        }
        fetchHeroes()
    }, [])



    const {skills} = GetCurrentHeroSkills({id: hero.id})
    const [show, setShow] = useState(false)
    const [className, setClassName] = useState('')
    useEffect(() => {
    if (show) {
      setClassName('visibleClass');
    } else {
      setClassName('');
    }
  }, [show]);




    return (
        <div>
        <div className={'current-hero'}>
            <HeroVideo hero={hero}/>

            <div className={'current-hero-info'} >
                <div className='hero-info'>
                    <HeroAttr id={hero.main_attribute}/>
                    <HeroType hero={hero} setShow={setShow} show={show}/>
                </div>

                <div className='hero-abilities'>
                    <div className='hero-talents'>
                        <img src={talents} alt="talents" className='talents' />
                        <CurrentHeroTalents hero={hero}/>
                    </div>
                    <div className='hero-skills'>
                        <h1>Abilities</h1>
                        <div className='hero-skill'>
                            {skills && skills.map((skill, index) => {
                                if (!(skill.ability_is_granted_by_scepter || skill.ability_is_granted_by_shard || skill.scepter_description || skill.shard_description))
                                return(
                                <HeroSkills key={skill.id} skill={skill}/>
                            )
                            })}
                        </div>
                    </div>
                </div>
            </div>
            <div className='current-hero-about'>
                <HeroAbout hero={hero}/>
            </div>
        </div>
            {hero && <CurrentHeroAspects hero={hero}/>}

        <CurrentHeroSkillsVideo skills={skills}/>
            <div className='nextPrev'>
                {prevHero && <PrevHero hero={prevHero}/>}
                <img className='allHeroes' src={allHeroes} alt="allHeroes" onClick={() => {window.location.href = '/heroes'}}/>
                {nextHero && <NextHero hero={nextHero}/>}
            </div>
    </div>
    )
}