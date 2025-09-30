"""

Ceci est le code menant au portfolio de Romain Traboul.

"""
# Import des librairies
import streamlit as st
import base64, mimetypes


# Charger les fichiers PDF
with open("Mémoire/Mémoire_Romain_Traboul.pdf", "rb") as file:
    memoire = file.read()

# Affichage du titre et du logo de l'application web
st.set_page_config(page_title="Portfolio Romain Traboul", page_icon="🧑‍💻", layout="wide")


# Titre de la page
st.markdown(
    "<h3 style='text-align: center;'>Portfolio de Romain Traboul</h3>", 
    unsafe_allow_html=True)

# Utilisation de st.columns pour centrer l'image
col1, col2, col3, col4, col5= st.columns([1, 1, 1, 1, 1])  # Création de trois colonnes

# Placer l'image dans la colonne du milieu
with col2:
    st.image("image/Photo_Romain_Traboul.jpg", width=500)

with col5:
    # Sélecteur de langue
    langue = st.radio("🌍 Choisissez votre langue / Choose your language :", ["Français", "English"])

# ---- CSS pour des lignes "icône + texte" responsives ----
st.markdown("""
<style>
.logo-row{
  display:flex; align-items:center; gap:10px; margin:6px 0;
}
.logo-row img{
  width:50px; height:50px; object-fit:contain; flex:0 0 50px;
}
.logo-row .text{ flex:1; }
@media (max-width: 480px){
  .logo-row{ gap:8px; }
  .logo-row img{ width:50px; height:50px; flex-basis:50px; }
}
</style>
""", unsafe_allow_html=True)

# ---------- Utilitaires ----------
@st.cache_data
def to_data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

def logo_row(icon_path: str, html_text: str, size: int | None = None, align: str = "center"):
    """
    - icon_path: chemin local de l'icône
    - html_text: contenu HTML (titres, <ul>, liens...)
    - size: taille px de l'icône (override ponctuel)
    - align: "center" (par défaut) ou "start" pour aligner en haut
    """
    src = to_data_uri(icon_path)
    size_style = f"width:{size}px;height:{size}px;flex:0 0 {size}px;object-fit:contain;" if size else ""
    align_style = "align-items:flex-start;" if align == "start" else "align-items:center;"
    st.markdown(
        f"""
        <div class="logo-row" style="{align_style}">
            <img src="{src}" alt="" style="{size_style}">
            <div class="text">{html_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Contenu basé sur la langue sélectionnée
if langue == "Français":
    # Section Contact
    with st.expander("📧 Profil"):
        logo_row("image/age_icon.png", "<strong>Âge</strong> : 25 ans (18/09/2000)", size=40)
        logo_row("image/email_icon.png", "<strong>Adresse mail</strong> : romain.traboul971@gmail.com", size=40)
        logo_row("image/linkedin_icon.png", '<a href="https://www.linkedin.com/in/romain-traboul-3bb8b4259" target="_blank"><strong>LinkedIn</strong></a>', size=40)
        logo_row("image/github_icon.png", '<a href="https://github.com/Twiist33" target="_blank"><strong>GitHub</strong></a>', size=40)
        logo_row("image/medium_icon.png", '<a href="https://medium.com/@romain.traboul971" target="_blank"><strong>Medium</strong></a>', size=40)
        logo_row("image/tableau_icon.png", '<a href="https://public.tableau.com/app/profile/romain.traboul/vizzes" target="_blank"><strong>Tableau</strong></a>', size=40)

    # Section Aptitudes
    with st.expander("💡 Aptitudes"):
        logo_row("image/programmation-logo.png","<strong>Langages de programmation / Outils de visualisation :</strong> Python, R, Excel, Tableau, Canva",size=40)
        logo_row("image/library-logo.png","<strong>Bibliothèques :</strong> Pandas, NumPy, Matplotlib, Streamlit, Beautifulsoup4, Selenium...",size=40)
        logo_row("image/sql-logo.png","<strong>Outils :</strong> PostgreSQL, Git",size=40)
        logo_row("image/ball-logo.png","<strong>Plateformes spécifiques à l'analyse sportive :</strong> SkillCorner, Statsbomb, LongoMatch",size=40)
        logo_row("image/langue-logo.png","<strong>Langues :</strong> Français (Natif), Anglais (C1)",size=40)

    # Section Expérience
    with st.expander("💼 Expérience"):
        logo_row(
            "image/logo_clermont_foot63.jpg",
            """
            <strong>Stagiaire Data Scientist</strong> au Clermont Foot 63 (Février 2024 - Juillet 2024)
            <div style="text-align: justify;">
            <ul>
                <li>Développement d’un modèle de deep learning pour évaluer la qualité des actions de jeu en fonction de leur probabilité de mener à un but, afin d’apporter une évaluation objective dans les rapports d’analyse de match</li>
                <li>Conception d’un modèle de deep learning de classification des phases de jeu, destiné à être intégré dans le système d’analyse du club et à contribuer à la préparation tactique pré et post-match</li>
            </ul>
            </div>
            """,
            size=60,           
            align="start"
        )

        logo_row(
            "image/logo_merignac_football.jpg",
            """
            <strong>Stagiaire Data Analyst</strong> au S.A Mérignac Football (Avril 2023 - Mai 2023)
            <div style="text-align: justify;">
            <ul>
                <li>Extraction et traitement de données statistiques issues de vidéos de match, en vue de constituer des jeux de données structurés exploitables pour l’analyse de performance</li>
                <li>Production de rapports statistiques destinés au staff technique, facilitant le suivi et la compréhension des performances de l’équipe pendant la période de compétition</li>
            </ul>
            </div>
            """,
            size=60,
            align="start"
        )

    # Section Formation
    with st.expander("🎓 Formation"):
        logo_row(
            "image/digisport-logo.png",
            """
            <strong>Master Science du Numérique et Sport</strong> — Université de Rennes 2 (2022–2024)<br>
            <em>Majeure : Sciences des données appliquées au sport</em>
            """,
            size=80, align="start"
        )
        logo_row(
            "image/mss_logo.png",
            """
            <strong>Master 1 Modélisation statistique et stochastique</strong> — Université de Bordeaux (2021–2022)
            """,
            size=80, align="start"
        )
        logo_row(
            "image/miashs_logo.png",
            """
            <strong>Licence MIASHS</strong> — Université de Bordeaux (2018–2021)<br>
            <em>Parcours : Sciences Cognitives</em>
            """,
            size=80, align="start"
        )

    # Section Projet
    with st.expander("🔨 Projets"):

        st.write(
            """
            - **Projet de Data Visualisation d'analyse des performances des joueurs des 5 grands championnats**
            <p style="text-align: justify;">
            L'objectif de ce projet est de <strong>visualiser les performances des joueurs sur la saison 24/25</strong>.
            Issus du travail de la communauté Kaggle, les données proviennent de :
            <ul>
                <li><a href="https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025" target="_blank">Fbref (Kaggle)</a></li>
                <li><a href="https://www.kaggle.com/datasets/davidcariboo/player-scores" target="_blank">Transfermarkt (Kaggle)</a></li>
            </ul>
            </p>

            <p style="text-align: justify;">
            Ainsi, l'analyse portera sur la saison 24/25 pour les compétitions suivantes :
            <strong>Ligue 1, Bundesliga, Premier League, La Liga, Serie A</strong>.
            </p>

            <br>

            <ul>
                <li><strong>📊 Analyse d'un Joueur</strong> : Analyse du joueur de votre choix à travers plusieurs statistiques</li>
                <li><strong>🥊 Comparaison entre Joueurs</strong> : Analyse comparative entre deux joueurs du même poste</li>
                <li><strong>🏆 Classement des joueurs (Stats Aggrégées par Catégorie) </strong> : Classement des joueurs par performance selon une statistique aggrégée par catégorie choisie</li>
                <li><strong>🥇 Classement des joueurs (Stats Brutes) </strong> : Classement des joueurs par performance selon une statistique brute choisie</li>
                <li><strong>🔎 Scouting </strong> : Établissement d'une liste de joueurs collant aux critères choisis</li>
            </ul>

            <br>

            Pour plus de détails sur ce projet, vous avez à votre disposition :
            <ul>
                <li><a href="https://player-performance-big-5-24-25-romain-traboul.streamlit.app/" target="_blank">Le lien de l'application</a></li>
                <li><a href="https://github.com/Twiist33/Player_Performance" target="_blank">Le code associé à l'application</a></li>
            </ul>
            """,
            unsafe_allow_html=True
        )
        
        # Ajout des images sous la section
        col1, col2 = st.columns(2)
        with col1:
            st.image("image/player_perf_fr.png", caption="Analyse d'un joueur", use_container_width=True)
        with col2:
            st.image("image/similarity_player_fr.png", caption="Analyse de joueurs similaires", use_container_width=True)

        col3, col4 = st.columns(2)
        with col3:
            st.image("image/comparative_radar_fr.png", caption="Analyse de deux joueurs", use_container_width=True)
        with col4:
            st.image("image/ranking_ast_fr.png", caption="Analyse d'une statistique", use_container_width=True)


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
            st.image("image/photo_competition_fr.jpg", caption="Analyse d'une compétition", use_container_width=True)
        with col2:
            st.image("image/photo_equipe_fr.jpg", caption="Analyse d'une équipe", use_container_width=True)

        # Ajout des images sous la section
        col3, col4 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col3:
            st.image("image/photo_saison_fr.jpg", caption="Analyse d'une saison", use_container_width=True)
        with col4:
            st.image("image/photo_confrontation_equipe_fr.jpg", caption="Analyse d'une opposition", use_container_width=True)



        st.write("""
            - **Autre projets**
                <ul>
                    <li><a href="https://public.tableau.com/app/profile/romain.traboul/viz/Big5Stats/Big5OffensivesStats">Dashboard sur les 5 grands championnats sur Tableau</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Dashboard_France_Argentine">Dashboard France_Argentine</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Visualisation_big_5">Visualisation sur les 5 grands championnats sur Python</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Dangerosité_Choc_Rugby">Projet Prediction Dangerosité Choc Rugby</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Score_du_match">Projet Prediction Score du match</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Behavior_team_score_season_15_16">Projet Analyse du Comportement des équipes selon le score</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Prediction_goals_24_25">Projet Prédiction Nombre de buts inscrits sur R</a></li>
                </ul>      
            """, unsafe_allow_html=True)

        # Ajout des images sous la section
        col5, col6 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col5:
            st.image("image/big5_stats_24_25.png", caption="Dashboard des statistiques sur les 5 grands championnats sur la saison 24/25 (Offensif)", use_container_width=True)
        with col6:
            st.image("image/diff_goals_xg_24_25.png", caption="Graphique des joueurs superformant le plus leur Xg sur la saison 24/25", use_container_width=True)
        
        col7, col8 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col7:
            st.image("image/Argentina_France_Dashboard.png", caption="Dashboard du match France-Argentine", use_container_width=True)
        with col8:
            st.image("image/Pizza_plot_Kylian_Mbappe.png", caption="Performance de Kylian Mbappe sur la saison 24/25", use_container_width=True)

        col9, col10 = st.columns(2)  # Création de deux colonnes pour aligner les images
        with col9:
            st.image("image/Rennes_team_dashboard.jpg", caption="Dashboard du comportement de Rennes selon le score sur la saison 15/16", use_container_width=True)
        with col10:
            st.image("image/Rennes_opponents_dashboard.jpg", caption="Dashboard du comportement des adversaires de Rennes selon le score sur la saison 15/16", use_container_width=True)

    # Section Articles
    with st.expander("📰 Articles"):

        st.markdown(
            """
        - <a href="https://medium.com/@romain.traboul971/le-1er-but-d%C3%A9termine-t-il-vraiment-lissue-d-un-match-74e908aeb887" target="_blank">
            <strong>Le 1er but détermine-t-il vraiment l’issue d’un match ? (16/09/2025)</strong>
        </a>
        <div style="text-align: justify;">
        Lors des grands événements sportifs comme les finales de Ligue des Champions ou la Coupe du Monde, on observe souvent que l’équipe qui marque en premier finit par l’emporter.
        Mais à quel point ce fameux premier but influence-t-il réellement l’issue d’un match ? Et quels en sont les facteurs déterminants ?
        C’est ce que je propose d’explorer à travers une analyse statistique et une revue de la littérature scientifique.
        </div>
        """,
            unsafe_allow_html=True
        )

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
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Création de six colonnes

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



else:
    # Contact Section
    with st.expander("📧 Profile"):
        logo_row("image/age_icon.png", "<strong>Age</strong>: 25 years old (18/09/2000)", size=40)
        logo_row("image/email_icon.png", "<strong>Email</strong>: romain.traboul971@gmail.com", size=40)
        logo_row("image/linkedin_icon.png", '<a href="https://www.linkedin.com/in/romain-traboul-3bb8b4259" target="_blank"><strong>LinkedIn</strong></a>', size=40)
        logo_row("image/github_icon.png", '<a href="https://github.com/Twiist33" target="_blank"><strong>GitHub</strong></a>', size=40)
        logo_row("image/medium_icon.png", '<a href="https://medium.com/@romain.traboul971" target="_blank"><strong>Medium</strong></a>', size=40)
        logo_row("image/tableau_icon.png", '<a href="https://public.tableau.com/app/profile/romain.traboul/vizzes" target="_blank"><strong>Tableau</strong></a>', size=40)

    # Skills Section
    with st.expander("💡 Skills"):
        logo_row("image/programmation-logo.png","<strong>Programming Languages / Visualization tools:</strong> Python, R, Excel, Tableau, Canva",size=40)
        logo_row("image/library-logo.png","<strong>Libraries:</strong> Pandas, NumPy, Matplotlib, Streamlit, BeautifulSoup4, Selenium...",size=40)
        logo_row("image/sql-logo.png","<strong>Tools:</strong> PostgreSQL, Git",size=40)
        logo_row("image/ball-logo.png","<strong>Sports Analysis Platforms:</strong> SkillCorner, StatsBomb, LongoMatch",size=40)
        logo_row("image/langue-logo.png","<strong>Languages:</strong> French (Native), English (C1)",size=40)

    # Experience Section
    with st.expander("💼 Experience"):
        logo_row(
            "image/logo_clermont_foot63.jpg",
            """
            <strong>Data Scientist Intern</strong> at Clermont Foot 63 (February 2024 – July 2024)
            <div style="text-align: justify;">
              <ul>
                <li>Developed a deep learning model to evaluate the quality of on-ball actions based on their probability of leading to a goal, enhancing the objectivity of match analysis reports shared with the coaching staff</li>
                <li>Built a deep learning model for classifying phases of play, designed to be integrated into the club’s analysis workflow and supporting pre- and post-match reporting</li>
              </ul>
            </div>
            """,
            size=60, align="start"
        )

        logo_row(
            "image/logo_merignac_football.jpg",
            """
            <strong>Data Analyst Intern</strong> at S.A Mérignac Football (April 2023 – May 2023)
            <div style="text-align: justify;">
              <ul>
                <li>Extracted and processed statistical data from match videos, transforming raw information into structured datasets for analysis</li>
                <li>Produced statistical reports that provided the coaching staff with quantified insights on team performance during the competition period</li>
              </ul>
            </div>
            """,
            size=60, align="start"
        )

    # ---------- Education Section ----------
    with st.expander("🎓 Education"):
        logo_row(
            "image/digisport-logo.png",
            """
            <strong>Master's Degree in Digital Science and Sports</strong> — Université de Rennes 2 (2022–2024)<br>
            <em>Major: Sports Data Science</em>
            """,
            size=80, align="start"
        )
        logo_row(
            "image/mss_logo.png",
            """
            <strong>Master 1 in Statistical and Stochastic Modeling</strong> — Université de Bordeaux (2021–2022)
            """,
            size=80, align="start"
        )
        logo_row(
            "image/miashs_logo.png",
            """
            <strong>Bachelor's Degree in MIASHS</strong> — Université de Bordeaux (2018–2021)<br>
            <em>Cognitive Science track</em>
            """,
            size=80, align="start"
        )

    # Projects Section
    with st.expander("🔨 Projects"):

        st.write(
            """
            - **Data visualisation project analysing player performance in the five major leagues**
            <p style="text-align: justify;">
            The goal of this project is to <strong>visualize player performances during the 24/25 season</strong>.
            Originally contributed by Kaggle users, the data comes from:
            <ul>
                <li><a href="https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025" target="_blank">Fbref dataset on Kaggle</a></li>
                <li><a href="https://www.kaggle.com/datasets/davidcariboo/player-scores" target="_blank">Transfermarkt dataset on Kaggle</a></li>
            </ul>
            </p>
            <p style="text-align: justify;">
            The analysis will cover the 24/25 season for the following competitions:
            <strong>Ligue 1, Bundesliga, Premier League, La Liga, Serie A</strong>.
            </p>

            <br>

            <ul>
                <li><strong>📊 Player Analysis</strong>: Analyze the player of your choice through various statistics</li>
                <li><strong>🥊 Player Comparison</strong>: Compare two players who play in the same position</li>
                <li><strong>🏆 Player Ranking (Aggregate Statistics by Category) </strong>: Rank players based on a chosen aggregate statistic by category</li>
                <li><strong>🥇 Player Ranking (Raw Statistics) </strong>: Rank players based on a chosen raw statistic</li>
                <li><strong>🔎 Scouting </strong> : Drawing up a list of players matching the chosen criteria</li>
            </ul>

            <br>

            For more details about this project, you can refer to:
            <ul>
                <li><a href="https://player-performance-big-5-24-25-romain-traboul.streamlit.app/" target="_blank">The link of the application</a></li>
                <li><a href="https://github.com/Twiist33/Player_Performance" target="_blank">The code associated with the application</a></li>
            </ul>
            """, unsafe_allow_html=True
        )
        # Add images below the section
        col1, col2 = st.columns(2)
        with col1:
            st.image("image/player_perf_eng.png", caption="Player performance analysis", use_container_width=True)
        with col2:
            st.image("image/similarity_player_eng.png", caption="Player performance similarity", use_container_width=True)

        col3, col4 = st.columns(2)
        with col3:
            st.image("image/comparative_radar_eng.png", caption="Radar comparison", use_container_width=True)
        with col4:
            st.image("image/ranking_ast_eng.png", caption="Statistical ranking analysis", use_container_width=True)

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
            st.image("image/photo_competition_eng.jpg", caption="Competition Analysis", use_container_width=True)
        with col2:
            st.image("image/photo_equipe_eng.jpg", caption="Team Analysis", use_container_width=True)

        col3, col4 = st.columns(2)  # Creating two columns to align images
        with col3:
            st.image("image/photo_saison_eng.jpg", caption="Season Analysis", use_container_width=True)
        with col4:
            st.image("image/photo_confrontation_equipe_eng.jpg", caption="Head-to-Head Analysis", use_container_width=True)


        st.write("""
            - **Other Projects**
                <ul>
                    <li><a href="https://public.tableau.com/app/profile/romain.traboul/viz/Big5Stats/Big5OffensivesStats">Dashboard of the Big 5 Leagues on Tableau</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Dashboard_France_Argentine">France-Argentina Dashboard</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Visualisation_big_5">Visualization of the Big 5 Leagues on Python</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Dangerosité_Choc_Rugby">Rugby Collision Danger Prediction Project</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Projet_Prediction_Score_du_match">Match Score Prediction Project</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Behavior_team_score_season_15_16">Project Analysis of behavior according the score</a></li>
                    <li><a href="https://github.com/Twiist33/Others_projects/tree/main/Prediction_goals_24_25">Project Prediction Number of goals scored on R</a></li>

                </ul>      
            """, unsafe_allow_html=True)

        # Adding images below the section
        col5, col6 = st.columns(2)  # Creating two columns to align images
        with col5:
            st.image("image/big5_stats_24_25.png", caption="Dashboard of statistics on the 5 major leagues for the 24/25 season (Offensive)", use_container_width=True)
        with col6:
            st.image("image/diff_goals_xg_24_25.png", caption="Graph of the players who superformed their Xg the most over the 24/25 season", use_container_width=True)
            
        col7, col8 = st.columns(2)  # Creating two columns to align images
        with col7:
            st.image("image/Argentina_France_Dashboard.png", caption="France-Argentina Match Dashboard", use_container_width=True)
        with col8:
            st.image("image/Pizza_plot_Kylian_Mbappe.png", caption="Kylian Mbappe's Performance in the 24/25 Season", use_container_width=True)

        col9, col10 = st.columns(2)  #Creating two columns to align images
        with col9:
            st.image("image/Rennes_team_dashboard.jpg", caption="Dashboard of Rennes' behaviour by score over the 15/16 season", use_container_width=True)
        with col10:
            st.image("image/Rennes_opponents_dashboard.jpg", caption="Dashboard of Rennes‘ opponents’ behaviour by score over the 15/16 season", use_container_width=True)

    # Section Articles
    with st.expander("📰 Articles"):

        st.markdown(
            """
    - <a href="https://medium.com/@romain.traboul971/le-1er-but-d%C3%A9termine-t-il-vraiment-lissue-d-un-match-74e908aeb887" target="_blank">
        <strong>Does the First Goal Really Decide the Outcome of a Match? (09/16/2025)</strong>
    </a>
    <div style="text-align: justify;">
    In major sporting events such as the Champions League finals or the World Cup, it is often observed that the team scoring first tends to win.  
    But to what extent does this crucial first goal truly influence the outcome of a match? And what are the determining factors behind it?  
    This is what I aim to explore through a statistical analysis and a review of the scientific literature.
    </div>
    """,
            unsafe_allow_html=True
        )

    # Section Mémoire
    with st.expander("📝 Dissertations"):
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
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Création de six colonnes

        # Utilisation du bouton pour télécharger le mémoire de M1
        with col3:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.download_button(
                label="Download M1",
                data=memoire,
                file_name="Mémoire_Romain_Traboul.pdf",
                mime="application/pdf"
            )
            st.markdown("</div>", unsafe_allow_html=True)

