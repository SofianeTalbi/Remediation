# On commence par importer les bibliotèques que nous allons utiliser
# Dash va nous permettre de créer notre dashboard
import dash
# On importe les composants de création de graphiques
from dash import dcc
# On importe les composants de création d'éléments HTML
from dash import html
# On importe les objets Input et Output pour définir des dépendances entre les composants Dash
from dash.dependencies import Input, Output
# On importe la bibliothèque Pandas sous l'alias "pd" pour pouvoir manipuler nos données
import pandas as pd
# On importe Plotly Express sous l'alias "px" pour créer des graphiques de manière simplifiée
import plotly.express as px
# On importe la partie "graph_objects" de Plotly pour créer des graphiques personnalisés
import plotly.graph_objects as go



# On commence par charger nos données
df1 = pd.read_csv('Electricity_Production_By_Source.csv')

# On crée une liste des pays européens car notre dashboard concerne uniquement les principaux pays européens
pays_europeens = ['France', 'Germany', 'United Kingdom', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands', 
                  'Belgium', 'Greece', 'Czechia', 'Portugal', 'Hungary', 'Sweden', 'Austria', 'Switzerland']

# On sélectionne les lignes correspondant aux pays européens
df_europe = df1[df1['Entity'].isin(pays_europeens)]

# On crée aussi une liste des années sur lequel nous allons travailler
annees_a_inclure = list(range(2010,2021))

# On sélectionnes les lignes correspondant aux années 2010 à 2020
df = df_europe[df_europe['Year'].isin(annees_a_inclure)]

# On crée une colonne pour la production électrique totale sur une année toutes sources confondu par pays
df['Total Electricity Production'] = df.iloc[:, 3:].sum(axis=1)



# On crée notre application Dash
app = dash.Dash(__name__)

# On importe notre fichier css pour améliorer légèrement le visuel de notre application (marge + dropdown coloré + font) 
app.css.append_css({
    'external_url': 'style.css'
})

# On crée une liste des années uniques dans notre jeu de donnée
years = df['Year'].unique()

# On crée une liste des sources d'électricités uniques
sources = [
    "Electricity from coal (TWh)",
    "Electricity from gas (TWh)",
    "Electricity from hydro (TWh)",
    "Electricity from other renewables (TWh)",
    "Electricity from solar (TWh)",
    "Electricity from oil (TWh)",
    "Electricity from wind (TWh)",
    "Electricity from nuclear (TWh)"
]

# On en crée une deuxième
energy_sources = [
    "Electricity from coal (TWh)",
    "Electricity from gas (TWh)",
    "Electricity from hydro (TWh)",
    "Electricity from other renewables (TWh)",
    "Electricity from solar (TWh)",
    "Electricity from oil (TWh)",
    "Electricity from wind (TWh)",
    "Electricity from nuclear (TWh)"
]

# On crée un dictionnaire sur lequel on associe chaque source d'energie à une icone
energy_icons = {
    "Electricity from coal (TWh)": "https://cdn-icons-png.flaticon.com/128/1275/1275575.png",
    "Electricity from gas (TWh)": "https://cdn-icons-png.flaticon.com/128/1658/1658010.png",
    "Electricity from hydro (TWh)": "https://cdn-icons-png.flaticon.com/128/5519/5519834.png",
    "Electricity from other renewables (TWh)": "https://cdn-icons-png.flaticon.com/128/4515/4515708.png",
    "Electricity from solar (TWh)": "https://cdn-icons-png.flaticon.com/128/4114/4114970.png",
    "Electricity from oil (TWh)":"https://cdn-icons-png.flaticon.com/128/1890/1890121.png",
    "Electricity from wind (TWh)":"https://cdn-icons-png.flaticon.com/128/5019/5019873.png",
    "Electricity from nuclear (TWh)": "https://cdn-icons-png.flaticon.com/128/5231/5231252.png"
}

# On aligne et on centre notre texte et nos icones sur notre dropdown des sources d'énergies
dropdown_options_energy = [
    {
        'label': html.Div([html.Img(src=energy_icons[source], style={'vertical-align': 'middle', 'margin-right': '10px', 'width': '20px'}), source]),
        'value': source
    }
    for source in sources
]

# On créer une liste des pays sur notre dataframe
countries = df['Entity'].unique()

# On crée un dictionnaire sur lequel on associe chaque pays à une icone
country_flags = {
    "France": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/langfr-338px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png",
    "Germany": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/langfr-338px-Flag_of_Germany.svg.png",
    "United Kingdom": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/langfr-338px-Flag_of_the_United_Kingdom_%283-5%29.svg.png",
    "Italy": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/langfr-338px-Flag_of_Italy.svg.png",
    "Spain": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/langfr-338px-Flag_of_Spain.svg.png",
    "Ukraine": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/langfr-338px-Flag_of_Ukraine.svg.png",
    "Poland": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/langfr-338px-Flag_of_Poland.svg.png",
    "Romania": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/langfr-338px-Flag_of_Romania.svg.png",
    "Netherlands": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/langfr-338px-Flag_of_the_Netherlands.svg.png",
    "Belgium": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/langfr-338px-Flag_of_Belgium_%28civil%29.svg.png",
    "Greece": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/langfr-338px-Flag_of_Greece.svg.png",
    "Czechia": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/langfr-338px-Flag_of_the_Czech_Republic.svg.png",
    "Portugal": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/langfr-338px-Flag_of_Portugal.svg.png",
    "Hungary": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_Hungary.svg/langfr-338px-Flag_of_Hungary.svg.png",
    "Sweden": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/langfr-338px-Flag_of_Sweden.svg.png",
    "Austria": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/langfr-338px-Flag_of_Austria.svg.png",
    "Switzerland": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/langfr-338px-Flag_of_Switzerland_%28Pantone%29.svg.png",
}

# On aligne et on centre notre texte et nos drapeaux sur notre dropdown des pays
dropdown_options = [
    {'label': html.Div([html.Img(src=f'{flag}', style={'vertical-align': 'middle', 'margin-right': '10px', 'width': '20px'}), country], style={'display': 'flex', 'align-items': 'center'}),
     'value': country}
    for country, flag in country_flags.items()
]

# On calcule la production d'électricité à partir de sources renouvelables et non renouvelables pour chaque année
df['Renewable Production (TWh)'] = df['Electricity from wind (TWh)'] + df['Electricity from solar (TWh)'] + df['Electricity from hydro (TWh)'] + df['Electricity from other renewables (TWh)']
df['Non-renewable Production (TWh)'] = df['Electricity from coal (TWh)'] + df['Electricity from gas (TWh)'] + df['Electricity from oil (TWh)'] + df['Electricity from nuclear (TWh)']

# On crée un dictionnaire qui associe chaque source d'énergie à sa production sur une année
total_production_by_source_yearly = {source: [] for source in sources}



app.layout = html.Div([
    # On crée le titre principal que l'on centre
    html.H1("Diversité des solutions de production électrique des principaux pays européens (+UK) entre 2010 et 2020", style={'text-align': 'center'}),

    html.Div([], style={'height': '25px'}),

    # On ecrit le titre de notre première partie
    html.H2("Production électrique en Europe par source et par année"),
    # On met une checklist et notre carte côte à côte
    html.Div([
        dcc.Checklist(
            id='map-source-checkbox',
            value=[sources[0]],
            options=dropdown_options_energy,    
            labelStyle={'display': 'block', 'margin-top': '10px'},  
        ),
    ], style={'width': '30%', 'float': 'left'}),
    html.Div([
        dcc.Graph(id='electricity-choropleth-map', style={'margin-top': '-15px'}), 
    ], style={'width': '70%', 'float': 'left'}),
    # On ajoute notre slider
    html.Div([
        dcc.Slider(
            id='map-year-slider',
            min=min(years),
            max=max(years),
            step=1,
            marks={str(year): str(year) for year in years},
            value=years[3]
        ),
    ], style={'width': '100%', 'float': 'left'}),


    # On ajoute un espace vertical en utilisant la marge supérieure
    html.Div([], style={'height': '500px'}),


    html.Div([
        html.H2("Répartition de la production d'électricité par source et par année"),
        html.Label("Sélectionnez la source d'électricité :"),
        dcc.Dropdown(
            id='source-dropdown',
            options=dropdown_options_energy,
            value=sources[2],
        ),

        # On crée notre diagramme en camembert
        dcc.Graph(id='electricity-pie-chart'),
        dcc.Slider(
            id='year-slider',
            min=min(years),
            max=max(years),
            step=1,
            marks={str(year): str(year) for year in years},
            value=years[8]
        ),
    ], style={'display': 'block'}),


    # On ajoute un espace vertical en utilisant la marge supérieure
    html.Div([], style={'height': '25px'}),


    html.Div([
        html.H2("Évolution de la production d'électricité d'une source de 2010 à 2020"),
        html.Label("Sélectionnez la source d'électricité :"),
        dcc.Dropdown(
            id='source-dropdown-2',
            options=dropdown_options_energy,
            value=sources[4],
        ),
        dcc.Graph(id='coal-production-line-chart')
    ], style={'display': 'block'}),


    # On ajoute un espace vertical en utilisant la marge supérieure
    html.Div([], style={'height': '10px'}),

 
    # On ajoute un graphique pour comparer la production d'électricité renouvelable et non renouvelable au fil des années pour un pays sélectionné
    html.Div([
        html.H2("Comparaison de la production d'électricité renouvelable (vent, soleil, eau, autres renouvelables) et non renouvelable (charbon, gaz, pétrole, nucléaire) par année"),
        html.Label("Sélectionnez le pays pour la comparaison renouvelable vs non renouvelable :"),
        dcc.Dropdown(
            id='country-dropdown-3',
            options=dropdown_options, 
            value=[list(country_flags.keys())[0]] + [list(country_flags.keys())[1]],
            multi=True,
            className='custom-dropdown'
        ),
        dcc.Graph(id='country-renewable-vs-nonrenewable-line-chart')
    ], style={'display': 'block'}),


    html.H2("Histogramme de la production électrique en Europe par source et par année"),
    html.Div([
        dcc.Checklist(
            id='map-source-checkbox_histogram',
            value=[sources[0]],
            options=dropdown_options_energy,    
            labelStyle={'display': 'block', 'margin-top': '10px'},
        ),
    ], style={'width': '30%', 'float': 'left'}),

    html.Div([
        dcc.Graph(id='electricity-total-histogram', style={'margin-top': '-15px'}), 
    ], style={'width': '70%', 'float': 'left'}), 

    html.Div([
        dcc.Slider(
            id='map-year-slider_histogram',
            min=min(years),
            max=max(years),
            step=1,
            marks={str(year): str(year) for year in years},
            value=years[3]
        ),
    ], style={'width': '100%', 'float': 'left'}),
    
    html.Div([
    dcc.Graph(id='total-production-line-chart')
], style={'width': '100%', 'float': 'left'})

])



# On fait des callback pour mettre à jour nos graphiques
@app.callback(
    Output('electricity-choropleth-map', 'figure'),
    [Input('map-year-slider', 'value'),
     Input('map-source-checkbox', 'value')]
)
def update_choropleth_map(selected_year, selected_sources):
    filtered_df = df[df['Year'] == selected_year]

    # On filtre les colonnes en fonction des sources sélectionnées et on additionne les valeurs
    filtered_df['Selected Sources'] = filtered_df[selected_sources].sum(axis=1)

    # On crée la carte choroplèthe
    fig = px.choropleth(
        filtered_df,
        locations="Entity",
        animation_frame="Year",
        locationmode="country names",
        color="Selected Sources",
        hover_name="Entity",
        title=f"<i>Production électrique en Europe par sources sélectionnées pour l'année {selected_year}</i>"
    )

    fig.update_layout(
    title={
        'x': 0.5  # On centre le titre horizontalement
    },
    title_font=dict(family="Arial"),
)
    # On définit la plage géographique pour l'Europe
    fig.update_geos(
        projection_type="natural earth",
        lataxis_range=[30, 80],  # Latitude : de 30 à 80 (couvrant l'Europe)
        lonaxis_range=[-30, 60]  # Longitude : de -30 à 60 (couvrant l'Europe)
    )

    return fig

@app.callback(
    Output('electricity-pie-chart', 'figure'),
    [Input('year-slider', 'value'), 
     Input('source-dropdown', 'value')]
)
def update_pie_chart(selected_year, selected_source):
    filtered_df = df[df['Year'] == selected_year]
    fig = px.pie(filtered_df, names='Entity', values=selected_source, title=f"Répartition de la production d'électricité par source en {selected_year}")
    fig.update_layout(title_text=f"<i>Répartition de la production d'électricité par source ({selected_source}) en {selected_year}</i>", title_font=dict(family="Arial"))
    return fig

@app.callback(
    Output('coal-production-line-chart', 'figure'),
    [Input('source-dropdown-2', 'value')]
)
def update_line_chart(selected_source):
    # On filtre les données pour la plage d'années de 2010 à 2020
    filtered_df = df[(df['Year'] >= 2010) & (df['Year'] <= 2020)]
    
    # On crée un graphique linéaire montrant l'évolution de la production d'électricité
    fig = px.line(
        filtered_df,
        x='Year',
        y=selected_source,
        color='Entity',
        labels={'Entity': 'Pays', selected_source: 'Production (TWh)'},
        markers=True,
        symbol='Entity'
    )
    return fig

@app.callback(
    Output('country-renewable-vs-nonrenewable-line-chart', 'figure'),
    [Input('country-dropdown-3', 'value')]
)
def update_country_renewable_vs_nonrenewable_chart(selected_countries):
    # On filtre les données pour les pays sélectionnés
    filtered_df = df[df['Entity'].isin(selected_countries)]

    # On regroupe les données par année et on somme la production pour chaque année
    grouped_df = filtered_df.groupby(['Year'])[['Renewable Production (TWh)', 'Non-renewable Production (TWh)']].sum().reset_index()

    # On crée un graphique linéaire pour comparer la production d'électricité renouvelable et non renouvelable au fil des années
    fig = px.line(
        grouped_df,
        x='Year',
        y=['Renewable Production (TWh)', 'Non-renewable Production (TWh)'],
        title="Comparaison de la production d'électricité renouvelable et non renouvelable pour les pays sélectionnés",
        labels={'Year': 'Année', 'value': 'Production (TWh)'},
        markers=True,
    )
    fig.update_layout(title_text="<i>Comparaison de la production d'électricité renouvelable et non renouvelable pour les pays sélectionnés</i>", title_font=dict(family="Arial"))
    return fig

@app.callback(
    Output('electricity-total-histogram', 'figure'),
    [Input('map-year-slider_histogram', 'value'),
     Input('map-source-checkbox_histogram', 'value')]
)
def update_total_histogram(selected_year, selected_sources):
    filtered_df = df[df['Year'] == selected_year]

    # On crée un dictionnaire pour stocker la production totale de chaque pays par source
    total_production_by_country = {}

    for source in selected_sources:
        total_production_by_country[source] = filtered_df.groupby('Entity')[source].sum()

    # On crée un dataframe à partir du dictionnaire
    total_production_df = pd.DataFrame(total_production_by_country)

    # On crée l'histogramme
    fig = px.bar(
        total_production_df,
        x=total_production_df.index,
        y=selected_sources,
        title=f"<i>Production électrique totale par source pour l'année {selected_year}</i>",
        labels={'index': 'Pays', 'value': 'Production (TWh)'}
    )

    fig.update_layout(
        title={
            'x': 0.5
        },
        title_font=dict(family="Arial"),
    )

    return fig

@app.callback(
    Output('total-production-line-chart', 'figure'),
    [Input('map-year-slider_histogram', 'value')]
)
def update_total_production_chart(selected_year):
    # On crée une liste vide pour chaque source pour stocker les valeurs de production année par année
    total_production_by_source_yearly = {source: [] for source in sources}
    
    for year in years:
        filtered_df = df[df['Year'] == year]

        # Pour chaque source, on calcule la somme de la production
        for source in sources:
            total_production = filtered_df[source].sum()
            total_production_by_source_yearly[source].append(total_production)

    # On crée le graphique
    fig = go.Figure()
    for source in sources:
        fig.add_trace(go.Scatter(x=years, y=total_production_by_source_yearly[source], mode='lines+markers', name=source))

    fig.update_layout(
        title=f"<i>Production électrique totale par source par année</i>",
        xaxis_title="Année",
        yaxis_title="Production électrique (TWh)",
        title_font=dict(family="Arial"),
        title_x=0.5  # Centre le titre horizontalement
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)