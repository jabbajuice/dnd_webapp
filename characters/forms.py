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
    
    # characterName = forms.CharField(label="Character Name", max_length=100)
    # Race = forms.ChoiceField(choices=RACE_CHOICES, label="Race")
    # Class = forms.ChoiceField(choices=CLASS_CHOICES, label="Class")
    # Strength = forms.IntegerField(label="Strength")
    # Dexterity = forms.IntegerField(label="Dexterity")
    # Constitution = forms.IntegerField(label="Constitution")
    # Intelligence = forms.IntegerField(label="Intelligence")
    # Wisdom = forms.IntegerField(label="Wisdom")
    # Charisma = forms.IntegerField(label="Charisma")
    # Skills = forms.CharField(widget=forms.Textarea, label="Skills")
    # Background = forms.CharField(widget=forms.Textarea, label="Background")
    # Equipment = forms.CharField(widget=forms.Textarea, label="Equipment")
    # Spells = forms.CharField(widget=forms.Textarea, label="Spells")
    # Appearance = forms.CharField(widget=forms.Textarea, label="Appearance")
    # Personality = forms.CharField(widget=forms.Textarea, label="Personality")

    # label_suffix = ""



    class Meta:
        model = Player_Characters
        fields = ('CharacterName','Race','Class','Strength','Dexterity','Constitution',
                  'Intelligence','Wisdom','Charisma','Skills','Background',
                  'Equipment','Spells','Appearance','PersonalityTraits')