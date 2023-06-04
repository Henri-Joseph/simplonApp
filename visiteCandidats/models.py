from django.db import models

# Creation du modèle pour la table candidat.
class Candidats(models.Model):
    id = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=20)
    firstname =  models.CharField(max_length=50)
    contact =  models.CharField(max_length=10)
    email =  models.EmailField()

    def __str__ (self):
        return "%s" %(self.lastname)
    
    class Meta:
        db_table="candidats"