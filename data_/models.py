from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator 
from django.db import models
from django.core.exceptions import ValidationError 
import random
import string


# Used to manage Data objects and group into one setting
class Trial(models.Model): 

	name = models.CharField(null=False,
														verbose_name="Name of trial",
														max_length=255)

	date = models.DateField()




# Used for recording basic data 
class Data(models.Model):

	# Seconds on data incoming 
	seconds = models.FloatField(null=True, 
																verbose_name="Seconds",
																default=0)
	# x-coordinate 
	x_coord = models.FloatField(null=True, 
																verbose_name="X",
																default=0)
	# y-coordinate 
	y_coord = models.FloatField(null=True, 
																verbose_name="Y", 
																default=0)
	# z-coordinate 
	z_coord = models.FloatField(null=True,
																verbose_name="Z",
																default=0)
	# Unknown metric 
	unknown = models.FloatField(null=True,
																verbose_name="Unknown",
																default=0)
	# Temperature 
	temp = models.FloatField(null=True,
														 verbose_name="Temperature",
														 default=0)
	# Electrodermal Activity (eda)
	eda = models.FloatField(null=True,
														verbose_name="EDA",
														default=0)

	# The raw tuple of the information flowing in 
	data_text = models.CharField(null=False, 
															 verbose_name="Piece of data",
															 max_length=270)


	# The trial this belongs to 
	trial = models.ForeignKey(Trial, default=None, null=True, on_delete=models.CASCADE)






