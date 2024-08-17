import streamlit as st
import pycaret
import pandas as pd
from pycaret.regression import *
loaded_model=load_model('C:/Users/anil.nagamunthala/TMDB/prediction')

genres=['History', 'Fantasy', 'Horror', 'Western', 'Thriller', 'Drama',
        'Science Fiction', 'Music', 'Documentary', 'Action', 'Animation',
        'TV Movie', 'Family', 'Mystery', 'Crime', 'War', 'Comedy', 'Romance', 'Adventure']

spoken_languages=['پښتو', 'English', 'isiZulu', 'Gaeilge', 'Türkçe', 'svenska', 'Český', 'עִבְרִית',
                  'Eesti', 'euskera', 'ქართული', 'Srpski', 'ελληνικά', 'Lietuvių', '普通话', 'Fulfulde',
                  'Română', 'Latin', 'Tiếng Việt', 'No Language', 'සිංහල', 'Italiano', 'Magyar', 'Somali',
                  'Slovenčina', '日本語', 'Português', 'Kiswahili', 'Afrikaans', 'Deutsch', 'Hrvatski',
                  'Français', 'हिन्दी', 'Pусский', 'فارسی', 'Polski', 'Norsk', 'shqip', 'العربية', 'தமிழ்',
                  '广州话 / 廣州話', 'Cymraeg', 'Dansk', 'اردو', 'Bahasa melayu', 'বাংলা', 'ภาษาไทย', 'Català',
                  'Nederlands', 'Esperanto', '한국어/조선말', 'suomi', 'български език', 'Íslenska', 'ਪੰਜਾਬੀ',
                  'Bosanski', 'Bahasa indonesia', 'Español', 'Український','Malti']

production_countries=['Australia', 'Dominican Republic', 'Israel', 'China', 'Morocco',
                      'Bulgaria', 'Canada', 'Iceland', 'Sweden', 'Japan', 'Botswana',
                      'Soviet Union', 'Indonesia', 'Serbia', 'United States of America',
                      'Russia', 'Malta', 'South Africa', 'Lebanon', 'Brazil', 'Montenegro',
                      'Turkey', 'Jamaica', 'Peru', 'India', 'Ukraine', 'Chile', 'Romania', 
                      'Libyan Arab Jamahiriya', 'Germany', 'Malaysia', 'Netherlands', 'Taiwan',
                       'Greece', 'Portugal', 'Ireland', 'Kenya', 'Singapore', 'Norway', 'Slovakia', 
                       'Mexico', 'Thailand', 'Zimbabwe', 'Saudi Arabia', 'Hungary', 'Austria', 'New Zealand',
                        'Spain', 'Aruba', 'United Kingdom', 'Italy', 'Luxembourg',
                        'Colombia', 'Finland', 'Denmark', 'France', 'Poland', 'United Arab Emirates', 
                        'Venezuela', 'Puerto Rico', 'Bahamas', 'Switzerland', 'Cyprus', 'South Korea',
                        'Belgium', 'Kuwait', 'Slovenia', 'Czech Republic', 'Hong Kong',
                        'Qatar','Nigeria','Albania','Macao','Namibia','Jordan','Yugoslavia','Palestinian Territory',
                        'Tunisia']
status={'Released':3 ,
        'Post Production': 2,
        'Planned':1,
        'In Production':0}

#dict values
movie_data={
 'id': 0,
 'budget': 0,
 'movie_url': ' ',
 'imdb_id': '',
 'movie_title': ' ',
 'overview': ' ',
 'popularity': 0,
 'poster_path': ' ',
 'production_companies': ' ',
 'runtime': 0,
 'tagline': ' ',
 'title': ' ' ,
 'keywords': ' ',
 'cast': ' ',
 'crew': ' ',
 'revenue': 0,
 'release_day': 0,
 'release_month': 0,
 'release_year': 0,
 'History': 0,
 'Fantasy': 0,
 'Horror': 0,
 'Western': 0,
 'Thriller': 0,
 'Drama': 0,
 'Science Fiction': 0,
 'Music': 0,
 'Documentary': 0,
 'Action': 1,
 'Animation': 0,
 'TV Movie': 0,
 'Family': 0,
 'Mystery': 0,
 'Crime': 0,
 'War': 0,
 'Comedy': 0,
 'Romance': 0,
 'Adventure': 0,
 'پښتو': 0,
 'English': 0,
 'isiZulu': 0,
 'Gaeilge': 0,
 'Türkçe': 0,
 'svenska': 0,
 'Český': 0,
 'עִבְרִית': 0,
 'Eesti': 0,
 'euskera': 0,
 'ქართული': 0,
 'Srpski': 0,
 'ελληνικά': 0,
 'Lietuvių': 0,
 '普通话': 0,
 'Fulfulde': 0,
 'Română': 0,
 'Latin': 0,
 'Tiếng Việt': 0,
 'No Language': 0,
 'සිංහල': 0,
 'Italiano': 0,
 'Magyar': 0,
 'Somali': 0,
 'Slovenčina': 0,
 '日本語': 0,
 'Português': 0,
 'Kiswahili': 0,
 'Afrikaans': 0,
 'Deutsch': 0,
 'Hrvatski': 0,
 'Français': 0,
 'हिन्दी': 0,
 'Pусский': 0,
 'فارسی': 0,
 'Polski': 0,
 'Norsk': 0,
 'shqip': 0,
 'العربية': 0,
 'தமிழ்': 0,
 '广州话 / 廣州話': 0,
 'Cymraeg': 0,
 'Dansk': 0,
 'اردو': 0,
 'Bahasa melayu': 0,
 'বাংলা': 0,
 'ภาษาไทย': 0,
 'Català': 0,
 'Nederlands': 0,
 'Esperanto': 0,
 '한국어/조선말': 0,
 'suomi': 0,
 'български език': 0,
 'Íslenska': 0,
 'ਪੰਜਾਬੀ': 0,
 'Bosanski': 0,
 'Bahasa indonesia': 0,
 'Español': 0,
 'Український': 0,
 'Australia': 0,
 'Dominican Republic': 0,
 'Israel': 0,
 'China': 0,
 'Morocco': 0,
 'Bulgaria': 0,
 'Canada': 0,
 'Iceland': 0,
 'Sweden': 0,
 'Japan': 0,
 'Botswana': 0,
 'Soviet Union': 0,
 'Indonesia': 0,
 'Serbia': 0,
 'United States of America': 0,
 'Russia': 0,
 'Malta': 0,
 'South Africa': 0,
 'Lebanon': 0,
 'Brazil': 0,
 'Montenegro': 0,
 'Turkey': 0,
 'Jamaica': 0,
 'Peru': 0,
 'India': 0,
 'Ukraine': 0,
 'Chile': 0,
 'Romania': 0,
 'Libyan Arab Jamahiriya': 0,
 'Germany': 0,
 'Malaysia': 0,
 'Netherlands': 0,
 'Taiwan': 0,
 'Greece': 0,
 'Portugal': 0,
 'Ireland': 0,
 'Kenya': 0,
 'Singapore': 0,
 'Norway': 0,
 'Slovakia': 0,
 'Mexico': 0,
 'Thailand': 0,
 'Zimbabwe': 0,
 'Saudi Arabia': 0,
 'Hungary': 0,
 'Austria': 0,
 'New Zealand': 0,
 'Spain': 0,
 'Aruba': 0,
 'United Kingdom': 0,
 'Italy': 0,
 'Luxembourg': 0,
 'Colombia': 0,
 'Finland': 0,
 'Denmark': 0,
 'France': 0,
 'Poland': 0,
 'United Arab Emirates': 0,
 'Venezuela': 0,
 'Puerto Rico': 0,
 'Bahamas': 0,
 'Switzerland': 0,
 'Cyprus': 0,
 'South Korea': 0,
 'Belgium': 0,
 'Kuwait': 0,
 'Slovenia': 0,
 'Czech Republic': 0,
 'Hong Kong': 0,
 'en': 0,
 'status_codes': 0,
 'Malti':0,
 'Albania':0,
 'Jordan':0,
 'Macao':0,
 'Namibia':0,
 'Nigeria':0,
 'Palestinian Territory':0,
 'Qatar':0,
 'Tunisia':0,
 'Yugoslavia':0}


#streamlit code
st.title('TMDB Movie Box Office Prediction')
movie_data['id']=st.number_input('Enter Movie ID')
movie_data['movie_title']=st.text_input('Enter Movie Title')
movie_data['movie_url']=st.text_input('Enter Movie URL')
overview_data=st.text_area("Enter Overview", height=5)
movie_data['overview']=overview_data
movie_data['popularity']=st.number_input('Enter Popularity')
movie_data['production_companies']=st.text_input('Production companies')
selected_pcountries=st.multiselect('Select Production Countries',production_countries)
for pcountries in selected_pcountries:
    movie_data[pcountries]=1

selected_spokenlanguages=st.multiselect('Select Spoken Language',spoken_languages)
for spokenlan in selected_spokenlanguages:
    movie_data[spokenlan]=1
release_dates=st.date_input('Release Date')
movie_data['release_day']=release_dates.day
movie_data['release_month']=release_dates.month
movie_data['release_year']=release_dates.year
movie_data['runtime']=st.number_input('Runtime (minutes)')
movie_data['budget']=st.number_input('Enter Budget ($)')
selected_genres=st.multiselect('Select Genres',genres)
for genre in selected_genres:
    movie_data[genre]=1
movie_data['imdb_id']=st.text_input('IMDB ID (Optional)')
selected_olan=st.selectbox('select Original language',['en'])
movie_data[selected_olan]=1
selected_status=st.selectbox('Select Status',['Released','Post Production','Planned','In Production'])
movie_data['status_codes']=status[selected_status]
movie_data['tagline']=st.text_input('Enter Tagline')
movie_data['keywords']=st.text_input('Enter Keywords')
movie_data['cast']=st.text_input('Enter Cast')
movie_data['crew']=st.text_input('Enter Crew')
val=movie_data['movie_title']
movie_data['title']=val
df=pd.DataFrame([movie_data])
def show_data():
    st.write('movie data')
    st.dataframe(movie_data)

if st.button('Predict Revenue') :
    
    show_data()
    predicted_revenue=predict_model(loaded_model,data=df)
    prediction=predicted_revenue['prediction_label']
    st.write(f"Predicted revenue:{prediction[0]}")
    st.balloons()
    

