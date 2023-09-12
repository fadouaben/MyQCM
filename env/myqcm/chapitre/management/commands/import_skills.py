import sqlite3
import requests
from bs4 import BeautifulSoup
import tabula
import pandas as pd
from django.core.management.base import BaseCommand
from chapitre.models import Skill
from django.apps import AppConfig
import xlrd
from django.conf import settings

class Command(BaseCommand):
    help = 'Import skills from PDF files'

    def handle(self, *args, **options):
        

        #récuperer les liens des pdfs

        url = "https://9raya.tn/%d9%85%d8%ae%d8%b7%d8%b7-%d8%a7%d9%84%d8%b1%d9%8a%d8%a7%d8%b6%d9%8a%d8%a7%d8%aa-%d8%a7%d9%84%d9%81%d8%aa%d8%b1%d8%a9-2/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        pdf_links = [link["href"] for link in soup.find_all("a") if link["href"].endswith(".pdf")]
        for linkpdf in pdf_links:
            print(linkpdf)

        merged_df = pd.DataFrame()

        for pdf_link in pdf_links:
            print(pdf_link)
            df = tabula.read_pdf(pdf_link,pages='all')[0]
            df.head()

            #data cleaning
            df_merged = df.groupby(df.index // 2).agg(lambda x: ' '.join(str(val) for val in x.dropna()))
            merged_df = pd.concat([merged_df,df_merged],axis=0)

        #réinitialiser les index 
        merged_df = merged_df.reset_index(drop=True)

        #enregistrer dataframe fusioné dans un fichier excel
        with pd.ExcelWriter('temp_merged.xlsx') as writer:
            merged_df.to_excel(writer,index=False)

        df = pd.read_excel('temp_merged.xlsx')
        skills_colonne = df.iloc[:, 3]
        for index,skill_data in skills_colonne.items():
            if pd.notna(skill_data):
                existing_skill = Skill.objects.filter(valeur=skill_data).first()

                if existing_skill is None:
                    # If the skill does not exist, create and save it
                    skill = Skill.objects.create(
                        valeur=skill_data,
                        niveau=6,
                        matiere='رياضيات'
                    )
                    skill.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported skills'))