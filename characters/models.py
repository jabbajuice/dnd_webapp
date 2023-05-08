from django.db import models 
from accounts.models import UserProfile

class Player_Characters(models.Model):
    RACE_CHOICES = (
    ("Human", "human"),
    ("Elf", "elf"),
    ("Dwarf", "dwarf"),
    ("Hafling","hafling"),
    ("Half-Elf","halfelf"),
    ("Half-Orc","halforc"),
    ("Orc","orc"),
    ("Gnome","gnome"),
    ("Tiefling","tiefling"),
    )

    CLASS_CHOICES = (
    ("Fighter","fighter"),
    ("Wizard", "wizard"),
    ("Rogue", "rogue"),
    ("Cleric","cleric"),
    ("Barbarian","barbarian"),
    ("Bard", "bard"),
    ("Druid", "druid"),
    ("Monk", "monk"),
    ("Paladin","paladin"),
    ("Ranger","ranger"),
    ("Sorcerer","sorcerer"),
    ("Warlock","warlock"), 
    )


    CharacterName = models.CharField(max_length=50)
    Race = models.CharField(max_length=30,choices = RACE_CHOICES)
    Class = models.CharField(max_length=30, choices=CLASS_CHOICES)
    Strength = models.IntegerField()
    Dexterity = models.IntegerField()
    Constitution = models.IntegerField()
    Intelligence = models.IntegerField()
    Wisdom = models.IntegerField()
    Charisma = models.IntegerField()
    Skills = models.TextField()
    Background = models.TextField()
    Equipment = models.TextField() 
    Spells = models.TextField()
    Appearance = models.TextField()
    PersonalityTraits = models.TextField()
    DateCreated = models.DateTimeField(auto_now_add=True)
    UserID = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=UserProfile.objects.latest('id').id if UserProfile.objects.exists() else None)

