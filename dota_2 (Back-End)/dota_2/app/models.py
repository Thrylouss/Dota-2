from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


# Create your models here.
class DatabaseState(models.Model):
    is_data_loaded = models.BooleanField(default=False)

    def __str__(self):
        return "Загружены ли данные: " + str(self.is_data_loaded)


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='attributes/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'


class Hero(models.Model):
    name = models.CharField(max_length=100)
    main_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    complexity = models.PositiveSmallIntegerField()
    advice = models.TextField()
    history = models.TextField()
    attack = models.JSONField()
    defense = models.JSONField()
    mobility = models.JSONField()
    hp = models.JSONField()
    mp = models.JSONField()
    attributes = models.JSONField()
    ATTACK_TYPE_CHOICES = [
        ('melee', 'Ближний бой'),
        ('ranged', 'Дальний бой'),
    ]
    attack_type = models.CharField(max_length=6, choices=ATTACK_TYPE_CHOICES)
    talents = models.JSONField()
    description = models.TextField()
    video = models.CharField(max_length=2222, null=True, blank=True)
    image = models.CharField(max_length=2222, null=True, blank=True)
    icon = models.CharField(max_length=2222, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class HeroRoles(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.hero}. {self.role}'

    class Meta:
        verbose_name = 'Hero role'
        verbose_name_plural = 'Hero roles'


class Aspects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=2222, null=True, blank=True)
    ability_description = models.TextField(null=True, blank=True)
    ability_name = models.CharField(max_length=100, null=True, blank=True)
    ability_icon = models.CharField(max_length=2222, null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Aspect'
        verbose_name_plural = 'Aspects'


class Skills(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=2222, null=True, blank=True)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()
    DAMAGE_TYPE_CHOICES = [
        ('physical', 'Physical'),
        ('magical', 'Magical'),
        ('pure', 'Pure'),
    ]
    damage_type = models.CharField(max_length=20,
                                   choices=DAMAGE_TYPE_CHOICES, null=True, blank=True)
    cooldown = models.CharField(max_length=100)
    mana_cost = models.CharField(max_length=100)
    spell_effects = models.JSONField()
    video = models.CharField(max_length=2222, null=True, blank=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    tip = models.TextField(null=True, blank=True)
    is_innate = models.BooleanField(default=False)
    ability_is_granted_by_shard = models.BooleanField(default=False)
    ability_is_granted_by_scepter = models.BooleanField(default=False)
    ability_has_scepter = models.BooleanField(default=False)
    ability_has_shard = models.BooleanField(default=False)
    scepter_description = models.TextField(blank=True, null=True)
    shard_description = models.TextField(blank=True, null=True)
    aghs_icon = models.CharField(max_length=2222, null=True, blank=True)
    is_facet = models.BooleanField(default=False)

    def clean_video_url(self):
        """Удаляет только дефис '-' из имени героя в поле video."""
        if self.video:
            parts = self.video.split('/abilities/')
            if len(parts) > 1:
                # Получаем часть после 'abilities/' и заменяем '-' на ''
                hero_part = parts[1].split('/')[0].replace('-', '')
                # Собираем обновленный URL
                self.video = parts[0] + '/abilities/' + hero_part + '/' + '/'.join(parts[1].split('/')[1:])
        return self.video

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
