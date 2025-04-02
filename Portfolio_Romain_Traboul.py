"""

Ceci est le code menant au portfolio de Romain Traboul.

"""
# Import des librairies
import streamlit as st

# Charger les fichiers PDF
with open("Mémoire/Mémoire_Romain_Traboul.pdf", "rb") as file:
    memoire = file.read()

# Affichage du titre et du logo de l'application web
st.set_page_config(page_title="Portfolio Romain Traboul", page_icon="🧑‍💻", layout="centered")

# Titre de la page
st.markdown(
    "<h3 style='text-align: center;'>Portfolio de Romain Traboul</h3>", 
    unsafe_allow_html=True)

# Utilisation de st.columns pour centrer l'image
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])  # Création de trois colonnes

# Placer l'image dans la colonne du milieu
with col3:
    st.image("image/Photo_Romain_Traboul.jpg", width=200)

with col6:
    # Sélecteur de langue
    langue = st.radio("🌍 Choisissez votre langue :", ["Français", "English"])

# Contenu basé sur la langue sélectionnée
if langue == "Français":
    # Section Contact
    with st.expander("📧 Informations personnelles"):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("image/age_icon.png", width=30)  # Icône pour l'âge
        with col2:
            st.write("**Âge** : 24 ans (18/09/2000)")

        col3, col4 = st.columns([1, 4])
        with col3:
            st.image("image/email_icon.png", width=30)  # Icône pour l'email
        with col4:
            st.write("**Adresse mail** : romain.traboul971@gmail.com")

        col5, col6 = st.columns([1, 4])
        with col5:
            st.image("image/linkedin_icon.png", width=30)  # Icône pour LinkedIn
        with col6:
            st.write("[**LinkedIn**](https://www.linkedin.com/in/romain-traboul-3bb8b4259)")

        col7, col8 = st.columns([1, 4])
        with col7:
            st.image("image/github_icon.png", width=30)  # Icône pour GitHub
        with col8:
            st.write("[**GitHub**](https://github.com/Twiist33)")


    # Section Expérience
    with st.expander("💼 Expérience"):
        col1, col2 = st.columns([1, 4])  # Une colonne large pour le texte, une plus petite pour l'image
        with col1:
            st.image("image/logo_clermont_foot63.jpg", width=60)  # Image à côté du texte
        with col2:
            st.write("""
            - **Stagiaire Data Scientist** au Clermont Foot 63 (Février 2024 - Juillet 2024)  
            <div style="text-align: justify;">
            Ma mission principale consistait à développer deux modèles distincts : un modèle pour évaluer la qualité des actions de jeu, et un autre pour classifier les phases de jeu.

            Grâce à l’utilisation conjointe des données d'événements et de tracking, l’objectif était de permettre une analyse globale d'une compétition ou d'une équipe sur ces aspects clés du football.
            </div> 
            """, unsafe_allow_html=True)

        col3, col4 = st.columns([1, 4])  
        with col3:
            st.image("image/logo_merignac_football.jpg", width=60)
        with col4:
            st.write("""
            - **Stagiaire Data Analyst** au S.A Mérignac Football (Avril 2023 - Mai 2023)
            <div style="text-align: justify;">
            À partir des vidéos de matchs et du logiciel LongoMatch, mon rôle était notamment d'extraire des données statistiques  
            afin de fournir un point de vue chiffré au staff sportif du club amateur.  
            Il m'arrivait également de compiler les actions de joueurs à la demande du staff.
            </div> 
            """, unsafe_allow_html=True)

    # Section Formation
    with st.expander("🎓 Formation"):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("image/digisport-logo.png", width=80)  # Icône ou logo de l'Université de Rennes 2
        with col2:
            st.write("""
            **Master Science du Numérique et Sport** à l'Université de Rennes 2 (2022 - 2024)  
            - Majeure Sciences des données appliquées au sport.
            """)

        col3, col4 = st.columns([1, 4])
        with col3:
            st.image("image/mss_logo.png", width=80)  # Icône ou logo de l'Université de Bordeaux
        with col4:
            st.write("""
            **Master 1 Modélisation statistique et stochastique** à l'Université de Bordeaux (2021 - 2022)
            """)

        col5, col6 = st.columns([1, 4])
        with col5:
            st.image("image/miashs_logo.png", width=80)  # Réutilisation du logo pour la Licence
        with col6:
            st.write("""
            **Licence MIASHS** à l'Université de Bordeaux (2018 - 2021)  
            - Parcours Sciences Cognitives
            """)

    # Section Projet
    with st.expander("🔨 Projets"):
        st.write("""
            - **Projet de Data Visualisation des championnats de football français**
            <div style="text-align: justify;">
            L'objectif de ce projet est de poursuivre le travail effectué lors de mon mémoire de M1 : <strong>Analyse comparative de 3 facteurs de performance dans le football : l'impact du 1er but, la distribution temporelle des buts et l’influence de l’avantage du terrain sur le match (domicile/extérieur) entre les équipes de jeunes (U17N et U19N)</strong>.  
            Ce mémoire s'articulant uniquement sur seulement 3 compétitions sur la saison 2022/2023, il m'a paru important d'étendre cette analyse en élargissant le nombre de compétitions et de saisons.  
            Ainsi, l'analyse prendra en compte les saisons récentes allant de 2021/2022 à 2024/2025 (lorsque cela est possible) et les compétitions suivantes : <strong>Ligue 1, Ligue 2, National 1, National 2, Championnat U19N, D1 Féminine et D2 Féminine</strong>.
            <br><br>


            Plusieurs fonctionnalités seront disponibles au sein de cette application web : 
            <ul>
                <li><strong>📊 Analyse d'une Équipe</strong> : Analyse du club de votre choix à travers plusieurs statistiques</li>
                <li><strong>🥊 Confrontation entre Équipes</strong> : Analyse comparative entre 2 équipes de votre choix d'une même saison</li>
                <li><strong>📅 Analyse d'une Saison</strong> : Aperçu des tendances sur une saison entière</li>
                <li><strong>🏆 Analyse d'une Compétition</strong> : Comparaison des indicateurs statistiques pour les compétitions de votre choix</li>
            </ul>
            
            <br><br>
            Pour plus de détails sur ce projet, vous avez à votre disposition :  
            <ul>
                <li><a href="https://datavizfrance-romain-traboul.streamlit.app/">Le lien de l'application web</a></li>
                <li><a href="https://github.com/Twiist33/Data_Viz_France">Le code associé à la création de l'application</a></li>
            </ul>
            </div>      
            """, unsafe_allow_html=True)
        
        # Ajout des images sous la section
        col1, col2 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col1:
            st.image("image/photo_competition.jpg", caption="Analyse d'une compétition", use_column_width=True)
        with col2:
            st.image("image/photo_equipe.jpg", caption="Analyse d'une équipe", use_column_width=True)

        # Ajout des images sous la section
        col3, col4 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col3:
            st.image("image/photo_saison.jpg", caption="Analyse d'une sasion", use_column_width=True)
        with col4:
            st.image("image/photo_confrontation_equipe.jpg", caption="Analyse d'une opposition", use_column_width=True)

        st.write("""
            - **Autre projets**
                <ul>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Dashboard_France_Argentine">Dashboard France_Argentine</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Visualisation_big_5">Visualisation sur les 5 grands championnats</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Dangerosité_Choc_Rugby">Projet Prediction Dangerosité Choc Rugby</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Score_du_match">Projet Prediction Score du match</a></li>
                </ul>      
            """, unsafe_allow_html=True)

        # Ajout des images sous la section
        col5, col6 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col5:
            st.image("image/Argentina_France_Dashboard.png", caption="Dashboard du match France-Argentine", use_column_width=True)
        with col6:
            st.image("image/Pizza_plot_Kylian_Mbappe.png", caption="Performance de Kylian Mbappe sur la saison 24/25", use_column_width=True)

    # Section Mémoire
    with st.expander("📝 Mémoires"):
        st.write("""

            - **Mémoire de M2 : Développement d'un modèle d'évaluation de la qualité d'une action dans le football**

            <div style="text-align: justify;">

            Dans l’objectif de quantifier objectivement la performance d’une équipe lors d’un match de football, de multiples statistiques avancées ont gagné en popularité ces dernières années. Toutefois, peu d’entre elles permettraient réellement d’évaluer les probabilités de but lors de chaque instant du match. Ce travail vise donc à concevoir un algorithme d’apprentissage des actions de jeu dans le football pour prédire le danger de but associé. 
            
            D’après la littérature scientifique, l’utilisation d’un modèle de réseaux de neurones en graphes pourrait se révéler pertinent et approprié en vue de tenir rigueur des relations entre les joueurs sur le terrain et le contexte de l’action en cours. Nous avons synchronisé les données de suivi des 22 joueurs sur le terrain avec l’information des évènements de jeu pour les saisons 2022/2023 et 2023/2024 de Ligue 1 et Ligue 2. 
            
            En variant le nombre de variable insérées dans le modèle, c’est celui incluant les informations sur les joueurs, leurs relations, et diverses caractéristiques contextuelles qui a obtenu les meilleures performances, avec une précision de 0.90 et une perte de 0.55. De plus, les variables axées sur la position des joueurs se sont révélées les plus influentes auprès du modèle, ce qui est en accord avec la littérature sur le sujet. 
            
            Les staffs professionnels pourraient ainsi utiliser cette métrique issue des réseaux de neurone en graphes lors de la préparation des matches pour maximiser les performances de leur équipe.
            
            **Mots clés** : Football, Évaluation d’une action de jeu, Apprentissage Profond, Réseau de neurones en graphes
            
            - **Mémoire de M1 : Analyse comparative de 3 facteurs de performance dans le football : l'impact du 1er but, la distribution temporelle des buts et l’influence de l’avantage du terrain sur le match (domicile/extérieur) entre les équipes de jeunes (U17N et U19N) et le monde professionnel (Ligue 1)**
    

            De nombreux indicateurs de performance en football sont couramment étudiés dans la littérature scientifique. Cependant, la majorité de ces études portent uniquement sur le football professionnel, et peu traitent des équipes de jeunes. Par conséquent, l'objectif de cette étude est d'analyser la répartition des buts marqués, l'influence du premier but inscrit et l'impact de l'avantage du terrain dans les championnats U19N, U17N et la Ligue 1 (première division professionnelle française) lors de la saison 2022-2023.
            
            L'échantillon de données comprend un total de 2 200 matchs, analysés selon les paramètres suivants : fréquence des buts marqués (par intervalles de 45 et 15 minutes), avantage du terrain et premier but inscrit. Un plus grand nombre de buts a été marqué en seconde période (54,41 %) et lors des 15 dernières minutes de jeu (21,90 %) dans ces trois compétitions.
            
            Le test du Chi-2 a révélé un impact significatif de l'influence du terrain et du premier but inscrit sur l'issue finale du match. En termes de ces deux paramètres, le championnat U19N présente les valeurs les plus élevées, tandis que les U17N et la Ligue 1 affichent des résultats relativement similaires. Bien que ces facteurs ne semblent pas évoluer de manière progressive avec l'âge, ces résultats sont globalement en accord avec des études similaires sur le sujet.
            
            Il convient de noter que les entraîneurs pourraient utiliser ces informations dans la préparation des matchs afin d'optimiser la performance de leur équipe.
            
            **Mots-clés** : But, Football, Compétition de jeunes, Analyse de performance
            
            </div>
            """, unsafe_allow_html=True)

        # Utilisation de st.columns pour afficher le bouton centré
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])  # Création de six colonnes

        # Utilisation du bouton pour télécharger le mémoire de M1
        with col3:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.download_button(
                label="Mémoire M1",
                data=memoire,
                file_name="Mémoire_Romain_Traboul.pdf",
                mime="application/pdf"
            )
            st.markdown("</div>", unsafe_allow_html=True)


    # Section Aptitudes
    with st.expander("💡 Aptitudes"):
        col1, col2 = st.columns([0.1, 0.9])  # Ajustement de la largeur des colonnes

        with col1:
            st.image("image/programmation-logo.png", width=30)
        with col2:
            st.write("**Langages de programmation :** Python, R, Excel")

        with col1:
            st.image("image/library-logo.png", width=30)
        with col2:
            st.write("**Bibliothèques :** Pandas, NumPy, Matplotlib, Streamlit, Beautifulsoup4, Selenium...")

        with col1:
            st.image("image/sql-logo.png", width=30)
        with col2:
            st.write("**Outils :** PostgreSQL, Git")

        with col1:
            st.image("image/ball-logo.png", width=30)
        with col2:
            st.write("**Plateformes spécifiques à l'analyse sportive :** SkillCorner, Statsbomb, LongoMatch")

        with col1:
            st.image("image/langue-logo.png", width=30)
        with col2:
            st.write("**Langues :** Français, Anglais")

else:
    # Contact Section
    with st.expander("📧 Personal Information"):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("image/age_icon.png", width=30)  # Icon for age
        with col2:
            st.write("**Age**: 24 years old (18/09/2000)")

        col3, col4 = st.columns([1, 4])
        with col3:
            st.image("image/email_icon.png", width=30)  # Icon for email
        with col4:
            st.write("**Email**: romain.traboul971@gmail.com")

        col5, col6 = st.columns([1, 4])
        with col5:
            st.image("image/linkedin_icon.png", width=30)  # Icon for LinkedIn
        with col6:
            st.write("[**LinkedIn**](https://www.linkedin.com/in/romain-traboul-3bb8b4259)")

        col7, col8 = st.columns([1, 4])
        with col7:
            st.image("image/github_icon.png", width=30)  # Icon for GitHub
        with col8:
            st.write("[**GitHub**](https://github.com/Twiist33)")

    # Experience Section
    with st.expander("💼 Experience"):
        col1, col2 = st.columns([1, 4])  # A smaller column for the image, a larger one for the text
        with col1:
            st.image("image/logo_clermont_foot63.jpg", width=60)  # Image next to the text
        with col2:
            st.write("""
            - **Data Scientist Intern** at Clermont Foot 63 (February 2024 - July 2024)
            <div style="text-align: justify;">
            My main mission was to develop two distinct models: a model to evaluate the quality of game actions, and another to classify game phases.

            By combining event and tracking data, the goal was to enable a comprehensive analysis of a competition or a team based on these key aspects of football.
            </div> 
            """, unsafe_allow_html=True)

        col3, col4 = st.columns([1, 4])  
        with col3:
            st.image("image/logo_merignac_football.jpg", width=60)
        with col4:
            st.write("""
            - **Data Analyst Intern** at S.A Mérignac Football (April 2023 - May 2023)
            <div style="text-align: justify;">
            Using match videos and the LongoMatch software, my role was mainly to extract statistical data  
            to provide a data-driven perspective to the club’s coaching staff.  
            I was also occasionally responsible for compiling player actions at the request of the staff.
            </div> 
            """, unsafe_allow_html=True)

    # Education Section
    with st.expander("🎓 Education"):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("image/digisport-logo.png", width=80)  # Icon or logo of Université de Rennes 2
        with col2:
            st.write("""
            **Master's Degree in Digital Science and Sports** at Université de Rennes 2 (2022 - 2024)  
            - Major in Sports Data Science.
            """)

        col3, col4 = st.columns([1, 4])
        with col3:
            st.image("image/mss_logo.png", width=80)  # Icon or logo of Université de Bordeaux
        with col4:
            st.write("""
            **Master 1 in Statistical and Stochastic Modeling** at Université de Bordeaux (2021 - 2022)
            """)

        col5, col6 = st.columns([1, 4])
        with col5:
            st.image("image/miashs_logo.png", width=80)  # Reuse the logo for the Bachelor's degree
        with col6:
            st.write("""
            **Bachelor's Degree in MIASHS** at Université de Bordeaux (2018 - 2021)  
            - Cognitive Science track
            """)

    # Projects Section
    with st.expander("🔨 Projects"):
        st.write("""
            - **Data Visualization Project on French Football Championships**
            <div style="text-align: justify;">
            The goal of this project is to continue the work carried out in my Master 1 thesis: <strong>Comparative analysis of three performance factors in football: the impact of the first goal, the temporal distribution of goals, and the influence of home advantage (home/away) among youth teams (U17N and U19N)</strong>.  
            Since this thesis focused solely on three competitions during the 2022/2023 season, I found it important to extend this analysis by increasing the number of competitions and seasons.  
            Thus, the analysis will cover recent seasons from 2021/2022 to 2024/2025 (when possible) and the following competitions: <strong>Ligue 1, Ligue 2, National 1, National 2, U19N Championship, D1 Féminine, and D2 Féminine</strong>.
            
            <br><br>
            Several features will be available in this web application:
            <ul>
                <li><strong>📊 Team Analysis</strong>: Analyze the club of your choice through various statistics</li>
                <li><strong>🥊 Team Comparison</strong>: Comparative analysis between two teams of your choice in the same season</li>
                <li><strong>📅 Season Analysis</strong>: Overview of trends throughout an entire season</li>
                <li><strong>🏆 Competition Analysis</strong>: Comparison of statistical indicators for selected competitions</li>
            </ul>
            <br><br>
            For more details on this project, you can access:  
            <ul>
                <li><a href="https://datavizfrance-romain-traboul.streamlit.app/">The web application link</a></li>
                <li><a href="https://github.com/Twiist33/Data_Viz_France">The code associated with the application's development</a></li>
            </ul>
            </div>      
            """, unsafe_allow_html=True)

        # Adding images below the section
        col1, col2 = st.columns(2)  # Creating two columns to align images
        with col1:
            st.image("image/photo_competition.jpg", caption="Competition Analysis", use_column_width=True)
        with col2:
            st.image("image/photo_equipe.jpg", caption="Team Analysis", use_column_width=True)

        col3, col4 = st.columns(2)  # Creating two columns to align images
        with col3:
            st.image("image/photo_saison.jpg", caption="Season Analysis", use_column_width=True)
        with col4:
            st.image("image/photo_confrontation_equipe.jpg", caption="Head-to-Head Analysis", use_column_width=True)

        st.write("""
            - **Other Projects**
                <ul>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Dashboard_France_Argentine">France-Argentina Dashboard</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Visualisation_big_5">Visualization of the Big 5 Leagues</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Dangerosité_Choc_Rugby">Rugby Collision Danger Prediction Project</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Score_du_match">Match Score Prediction Project</a></li>
                </ul>      
            """, unsafe_allow_html=True)

        # Adding images below the section
        col5, col6 = st.columns(2)  # Creating two columns to align images
        with col5:
            st.image("image/Argentina_France_Dashboard.png", caption="France-Argentina Match Dashboard", use_column_width=True)
        with col6:
            st.image("image/Pizza_plot_Kylian_Mbappe.png", caption="Kylian Mbappe's Performance in the 24/25 Season", use_column_width=True)

    # Section Mémoire
    with st.expander("📝 Mémoires"):
        st.write("""

            - **Master’s 2 dissertation : Development of a model for evaluating the quality of a soccer play**

            <div style="text-align: justify;">

            With the aim of objectively quantifying a team's performance in a soccer match, many advanced statistics have gained in popularity in recent years. However, few of them are really able to evaluate the probability of scoring a goal at each moment of the match. The aim of this work is therefore to design a learning algorithm for soccer play actions to predict the associated goal danger. According to the scientific literature, the use of a graph-based neural network model could prove relevant and appropriate for taking into account the relationships between the players on the pitch and the context of the action in progress. We synchronized the tracking data of the 22 players on the pitch with game event information for the 2022/2023 and 2023/2024 Ligue 1 and Ligue 2 seasons. Varying the number of variables inserted into the model, the one including information on players, their relationships, and various contextual features performed best, with 90% accuracy and 0.55 loss. What's more, the variables focusing on player position proved the most influential with the model, which is in line with the literature on the subject. Professional staffs could therefore use this metric, derived from graphical neural networks, to improve the performance of their teams.
            **Key words** : Soccer, Valuing Action, Deep learning, Graph neural network
            
            - **Master’s 1 dissertation : Comparative analysis of 3 performance factors in football: the impact of the 1st goal, the timing of goals and the influence of the field advantage on the match (home/away) between youth teams (U17N and U19N) and the professional world (Ligue 1)**
    

            Numerous performance indicators in soccer are commonly studied in the scientific literature. However, most of these studies concern only professional soccer, and few deal with youth teams. Consequently, the aim of this study is to analyze the distribution of goals scored, the influence of the 1st goal and the impact of home advantage in the U19N, U17N and top-level French professional leagues (Ligue 1) for the 2022-2023 season. The data sample comprises a total of 2,200 matches, which were analyzed using the following parameters: frequency of goals scored (at intervals of 45 and 15 minutes), home advantage and 1st goal scored. More goals were scored in the 2nd half (54.41%) and during the last 15 minutes of play (21.90%) for these 3 competitions. The Chi-2 test revealed a significant impact of the influence of the pitch and the 1st goal on the final outcome of the match. In terms of these two parameters, the U19N had the highest scores, while the U17N and Ligue 1 leagues had relatively similar values. Although these factors would not be progressive with age, these results would appear to be broadly in line with similar studies on the subject. It should be noted that coaches could use this information in match preparation, to maximize their team's performance.
            
            **Key words** : Goal, Football, Youth competition, Performance analysis
            
            </div>
            """, unsafe_allow_html=True)

        # Utilisation de st.columns pour afficher le bouton centré
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])  # Création de six colonnes

        # Utilisation du bouton pour télécharger le mémoire de M1
        with col3:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.download_button(
                label="M1",
                data=memoire,
                file_name="Mémoire_Romain_Traboul.pdf",
                mime="application/pdf"
            )
            st.markdown("</div>", unsafe_allow_html=True)

    # Skills Section
    with st.expander("💡 Skills"):
        col1, col2 = st.columns([0.1, 0.9])  # Adjusting column width

        with col1:
            st.image("image/programmation-logo.png", width=30)
        with col2:
            st.write("**Programming Languages:** Python, R, Excel")

        with col1:
            st.image("image/library-logo.png", width=30)
        with col2:
            st.write("**Libraries:** Pandas, NumPy, Matplotlib, Streamlit, BeautifulSoup4, Selenium...")

        with col1:
            st.image("image/sql-logo.png", width=30)
        with col2:
            st.write("**Tools:** PostgreSQL, Git")

        with col1:
            st.image("image/ball-logo.png", width=30)
        with col2:
            st.write("**Sports Analysis Platforms:** SkillCorner, StatsBomb, LongoMatch")

        with col1:
            st.image("image/langue-logo.png", width=30)
        with col2:
            st.write("**Languages:** French, English")
