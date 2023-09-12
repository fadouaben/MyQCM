from django.apps import AppConfig
import sqlite3
from bs4 import BeautifulSoup
import requests
import tabula 
import pandas as pd
import xlrd
from django.conf import settings


class ChapitreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chapitre'
    def ready(self) :
        #cinnexion db



        return super().ready()
