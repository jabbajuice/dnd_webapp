from django import forms    
from characters.models import Player_Characters

class CharacterForm(forms.ModelForm):

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
    
    characterName = forms.CharField(label="Character Name", max_length=100)
    race = forms.ChoiceField(choices=RACE_CHOICES,label="Race")
    classType = forms.ChoiceField(choices=CLASS_CHOICES,label="Class Type")
    strength = forms.IntegerField(label="Strength:")
    dexterity = forms.IntegerField(label="Dexterity:")
    constitution = forms.IntegerField(label="Constitution:")
    intelligence = forms.IntegerField(label="Intelligence:")
    wisdom = forms.IntegerField(label="Wisdom:")
    charisma = forms.IntegerField(label="Charisma:")
    skills = forms.IntegerField(label="Skills:")
    background = forms.TextInput(label="Background")
    equipment = forms.TextInput(label="Equipment")
    spells = forms.TextInput(label="Spells")
    appearance = forms.TextInput(label="Appearance")
    personalityTraits = forms.TextInput(label="Personality Traits")

    class Meta:
        model = Player_Characters
        fields = ('Race','Class','Strength','Dexterity','Constitution',
                  'Intelligence','Wisdom','Charisma','Skills','Background',
                  'Equipment','Spells','Appearance','Personality Traits')