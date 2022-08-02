import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox
import time
import os
import pyaztro
import json

root= Tk()
root.geometry('750x550')
root.configure(bg='#262626')
#root.resizable(0,0)
root.title('News DashBoard By Erdeniz Unvan')

def main_menu():
    menu_frame.place(x=0,y=63)

def news():
    hide()
    news_frame.place(x=300,y=0)

def bring_news():
    country=country_combo.get()
    if country=='United Arab Emirates':
        country=country.replace('United Arab Emirates','ae')
    elif country=='Argentina':
        country=country.replace('Argentina','ar')
    elif country=='Austria':
        country=country.replace('Austria','at')
    elif country=='Australia':
        country=country.replace('Australia','au')
    elif country=='Belgium':
        country=country.replace('Belgium','be')
    elif country=='Bulgaria':
        country=country.replace('Bulgaria','bg')
    elif country=='Brazil':
        country=country.replace('Brazil','ae')
    elif country=='Canada':
        country=country.replace('Canada','ca')
    elif country=='Switzerland':
        country=country.replace('Switzerland','ch')
    elif country=='China':
        country=country.replace('China','cn')
    elif country=='Colombia':
        country=country.replace('Colombia','co')
    elif country=='Cuba':
        country=country.replace('Cuba','cu')
    elif country=='Czechia':
        country=country.replace('Czechia','cz')
    elif country=='Germany':
        country=country.replace('Germany','de')
    elif country=='Egypt':
        country=country.replace('Egypt','eg')
    elif country=='France':
        country=country.replace('France','fr')
    elif country=='England':
        country=country.replace('England','gb')
    elif country=='Greece':
        country=country.replace('Greece','gr')
    elif country=='Hong Kong':
        country=country.replace('Hong Kong','hk')
    elif country=='Hungary':
        country=country.replace('Hungary','hu')
    elif country=='Indonesia':
        country=country.replace('Indonesia','id')
    elif country=='Ireland':
        country=country.replace('Ireland','ie')
    elif country=='Israel':
        country=country.replace('Israel','il')
    elif country=='India':
        country=country.replace('India','in')
    elif country=='Italy':
        country=country.replace('Italy','it')
    elif country=='Japan':
        country=country.replace('Japan','jp')
    elif country=='South Korea':
        country=country.replace('South Korea','kr')
    elif country=='Lithuania':
        country=country.replace('Lithuania','lt')
    elif country=='Latvia':
        country=country.replace('Latvia','lv')
    elif country=='Morocco':
        country=country.replace('Morocco','ma')
    elif country=='Mexico':
        country=country.replace('Mexico','mx')
    elif country=='Malaysia':
        country=country.replace('Malaysia','my')
    elif country=='Nigeria':
        country=country.replace('Nigeria','ng')
    elif country=='Netherlands':
        country=country.replace('Netherlands','nl')
    elif country=='Norway':
        country=country.replace('Norway','no')
    elif country=='New Zealand':
        country=country.replace('New Zealand','nz')
    elif country=='Philippines':
        country=country.replace('Philippines','ph')
    elif country=='Poland':
        country=country.replace('Poland','pl')
    elif country=='Portugal':
        country=country.replace('Portugal','pt')
    elif country=='Romania':
        country=country.replace('Romania','ro')
    elif country=='Serbia':
        country=country.replace('Serbia','rs')
    elif country=='Russia':
        country=country.replace('Russia','ru')
    elif country=='Saudi Arabia':
        country=country.replace('Saudi Arabia','sa')
    elif country=='Sweden':
        country=country.replace('Sweden','se')
    elif country=='Singapore':
        country=country.replace('Singapore','sg')
    elif country=='Slovenia':
        country=country.replace('Slovenia','si')
    elif country=='Slovakia':
        country=country.replace('Slovakia','sk')
    elif country=='Thailand':
        country=country.replace('Thailand','th')
    elif country=='Türkiye':
        country=country.replace('Türkiye','tr')
    elif country=='Taiwan':
        country=country.replace('Taiwan','tw')
    elif country=='Ukraine':
        country=country.replace('Ukraine','ua')
    elif country=='United States':
        country=country.replace('United States','us')
    elif country=='Venezuela':
        country=country.replace('Venezuela','ve')
    elif country=='South Africa':
        country=country.replace('South Africa','za')
    api='d62b3b460dd043a98adcfbf848d709e0'
    url='https://newsapi.org/v2/top-headlines'
    query_params = {'apiKey':api,
                    'country':country,
                    'category':category_combo.get(),
                    'q':query_entry.get()}
    response = requests.get(url,params=query_params)
    news = response.json()['articles']
    if len(news)==0:
        messagebox.showwarning("No news have been found",'Sorry, we could not find any news regarding your parameters.\nPlease try again with different parameters')

    elif len(news)==1:
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}'''
    
    elif len(news)==2:
         result =f'''
        Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}'''
    
    elif len(news)==3:
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}'''
    
    elif len(news)==4:
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}'''
    
    elif len(news)==5:
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}'''    
     
    elif len(news) == 6:   
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}
        
        News:6 / Title: {response.json()['articles'][5]['title']}
        Description: {response.json()['articles'][5]['description']}
        Url: {response.json()['articles'][5]['url']}
        '''
    elif len(news) == 7:   
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}
        
        News:6 / Title: {response.json()['articles'][5]['title']}
        Description: {response.json()['articles'][5]['description']}
        Url: {response.json()['articles'][5]['url']}
        
        News:7 / Title: {response.json()['articles'][6]['title']}
        Description: {response.json()['articles'][6]['description']}
        Url: {response.json()['articles'][6]['url']}
        '''
    elif len(news) == 8:   
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}
        
        News:6 / Title: {response.json()['articles'][5]['title']}
        Description: {response.json()['articles'][5]['description']}
        Url: {response.json()['articles'][5]['url']}
        
        News:7 / Title: {response.json()['articles'][6]['title']}
        Description: {response.json()['articles'][6]['description']}
        Url: {response.json()['articles'][6]['url']}
        
        News:8 / Title: {response.json()['articles'][7]['title']}
        Description: {response.json()['articles'][7]['description']}
        Url: {response.json()['articles'][7]['url']}
        '''
    elif len(news) == 9:   
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}
        
        News:6 / Title: {response.json()['articles'][5]['title']}
        Description: {response.json()['articles'][5]['description']}
        Url: {response.json()['articles'][5]['url']}
        
        News:7 / Title: {response.json()['articles'][6]['title']}
        Description: {response.json()['articles'][6]['description']}
        Url: {response.json()['articles'][6]['url']}
        
        News:8 / Title: {response.json()['articles'][7]['title']}
        Description: {response.json()['articles'][7]['description']}
        Url: {response.json()['articles'][7]['url']}
        
        News:9 / Title: {response.json()['articles'][8]['title']}
        Description: {response.json()['articles'][8]['description']}
        Url: {response.json()['articles'][8]['url']}
        '''
    elif len(news) >= 10:   
        result =f'''
        News:1/ Title: {response.json()['articles'][0]['title']}
        Description: {response.json()['articles'][0]['description']}
        Url: {response.json()['articles'][0]['url']}

        News:2 / Title: {response.json()['articles'][1]['title']}
        Description: {response.json()['articles'][1]['description']}
        Url: {response.json()['articles'][1]['url']}

        News:3 / Title: {response.json()['articles'][2]['title']}
        Description: {response.json()['articles'][2]['description']}
        Url: {response.json()['articles'][2]['url']}

        News:4 / Title: {response.json()['articles'][3]['title']}
        Description: {response.json()['articles'][3]['description']}
        Url: {response.json()['articles'][3]['url']}

        News:5 / Title: {response.json()['articles'][4]['title']}
        Description: {response.json()['articles'][4]['description']}
        Url: {response.json()['articles'][4]['url']}
        
        News:6 / Title: {response.json()['articles'][5]['title']}
        Description: {response.json()['articles'][5]['description']}
        Url: {response.json()['articles'][5]['url']}
        
        News:7 / Title: {response.json()['articles'][6]['title']}
        Description: {response.json()['articles'][6]['description']}
        Url: {response.json()['articles'][6]['url']}
        
        News:8 / Title: {response.json()['articles'][7]['title']}
        Description: {response.json()['articles'][7]['description']}
        Url: {response.json()['articles'][7]['url']}
        
        News:9 / Title: {response.json()['articles'][8]['title']}
        Description: {response.json()['articles'][8]['description']}
        Url: {response.json()['articles'][8]['url']}
        
        News:10 / Title: {response.json()['articles'][9]['title']}
        Description: {response.json()['articles'][9]['description']}
        Url: {response.json()['articles'][9]['url']}
        '''     
    messagebox.showinfo('Press Ok to Quit',result)

def exit():
    root.destroy()

def submit():
    pass

def weather():
    hide()
    weather_frame.place(x=300,y=0)

def hide():
    news_frame.place_forget()
    weather_frame.place_forget()
    bitcoin_frame.place_forget()
    currency_frame.place_forget()
    horoscope_frame.place_forget()

def submit():
    city = weather_city_name_entry.get()
    if city=='' or city==' ':
        messagebox.showinfo('No city name is typed' ,'Please type a city name in order to proceed')


    else:
        try:    
            if city.isupper():
                city = city[0].upper() + city[1:].lower()
                
            elif city.islower():
                city = city[0].upper() + city[1:].lower()

            url='https://api.openweathermap.org/data/2.5/weather'
            apikey='97afb3c84a9f644b9bd5b9586ea5497a'
            query_params ={'id':open_weather[city],'appid':apikey,'units':'metric'}
            response = requests.get(url,params=query_params,verify=False)

        except Exception as e:

            messagebox.showinfo('Wrong City' ,f'No city by name of {city}')

        else:
            temperature = response.json()['main']['temp']
            messagebox.showinfo(f'City: {city}.',f'Date: {time.ctime()[4:10]+" "+time.ctime()[-4:]}. Time: {time.ctime()[11:20]}. Celcius: {temperature}')


def bitcoin():
    hide()
    bitcoin_frame.place(x=300,y=0)

def bc():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url='https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url,verify=False)
    message=f'''
    1 Bitcoin is:
    $: {response.json()["bpi"]["USD"]["rate"]}
    €: {response.json()["bpi"]["EUR"]["rate"]}
    £: {response.json()["bpi"]["GBP"]["rate"]}
    Date:
    {time.ctime()[4:10]+' '+time.ctime()[-4:]}
    Time:
    {time.ctime()[11:20]}
    '''
    bitcoin_label = Label(bitcoin_frame,text=message,font=helv36,fg="white",bg='#ff704d')
    bitcoin_label.place(x=120,y=261)

def currency():
    hide()
    currency_frame.place(x=300,y=0)

def cr():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url1='https://api.fastforex.io//fetch-one?from=USD&to=TRY&api_key=abebf3d412-4f462f1db9-rf5ykp'
    response1 = requests.get(url1,verify=False)
    url2='https://api.fastforex.io//fetch-one?from=EUR&to=TRY&api_key=abebf3d412-4f462f1db9-rf5ykp'
    response2 = requests.get(url2,verify=False)
    url3='https://api.fastforex.io//fetch-one?from=GBP&to=TRY&api_key=abebf3d412-4f462f1db9-rf5ykp'
    response3 = requests.get(url3,verify=False)
    message1=f'''
    1$ : {response1.json()['result']['TRY']} TRY
    1€ : {response2.json()['result']['TRY']} TRY
    1£ : {response3.json()['result']['TRY']} TRY
    Date:
    {time.ctime()[4:10]+' '+time.ctime()[-4:]}
    Time:
    {time.ctime()[11:20]}
    '''

    currency_label = Label(currency_frame,text=message1,font=helv36,fg="white",bg='#4dff4d')
    currency_label.place(x=120,y=261)

def horoscope():
    hide()
    horoscope_frame.place(x=300,y=0)

def hr():
    SIGN=horoscope_combo.get()
    horoscope = pyaztro.Aztro(sign=SIGN)
    date=horoscope.current_date
    mood=horoscope.mood
    daily=horoscope.description
    message=f'''
    
    Date: {time.ctime()[4:10]+' '+time.ctime()[-4:]}
    Your mood: {mood}
    Your Daily Horoscope:{daily}
    
    '''
    messagebox.showinfo(f"Daily Horoscope of {SIGN} for {time.ctime()[4:10]+' '+time.ctime()[-4:]} ",message)

helv36 = font.Font(family='Helvetica',size=16, weight='bold')

menu_frame = Frame(root,width=300, height=550,bg='#12c4c0')
b1 = Button(menu_frame,text='N E W S',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=news)
b1['font']=helv36
b1.place(x=0,y=150)
b2 = Button(menu_frame,text='W E A T H E R',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=weather)
b2['font']=helv36
b2.place(x=0,y=190)
b3 = Button(menu_frame,text='B I T C O I N',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=bitcoin)
b3['font']=helv36
b3.place(x=0,y=224)
b4 = Button(menu_frame,text='$ € £ ₺',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=currency)
b4['font']=helv36
b4.place(x=0,y=261)
b5 = Button(menu_frame,text='H O R O S C O P E',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=horoscope)
b5['font']=helv36
b5.place(x=0,y=298)
b6 = Button(menu_frame,text='E X I T',width=20,height=1,fg='#666699',border=0,bg='#12c4c0',activeforeground='#262626',
activebackground='#0f9d9a',command=exit)
b6['font']=helv36
b6.place(x=0,y=335)
  
news_frame=Frame(root,width=450, height=550,bg='#999966')
news_label=Label(news_frame, text = 'Select Country',font=helv36,fg="white",bg='#999966')
news_label.place(x=10,y=150)
country_options =['United Arab Emirates','Argentina','Austria','Australia',
'Belgium','Bulgaria','Brazil','Canada','Switzerland','China'
,'Colombia','Cuba','Czechia','Germany','Egypt','France','England','Greece'
,'Hong Kong','Hungary','Indonesia','Ireland','Israel','India','Italy'
,'Japan','South Korea','Lithuania','Latvia','Morocco','Mexico','Malaysia'
,'Nigeria','Netherlands','Norway','New Zealand','Philippines','Poland'
,'Portugal','Romania','Serbia','Russia','Saudi Arabia','Sweden'
,'Singapore','Slovenia','Slovakia','Thailand','Türkiye','Taiwan'
,'Ukraine','United States','Venezuela','South Africa']
country_combo = ttk.Combobox(news_frame, value=country_options,font=helv36)
country_combo.current(0)
country_combo.place(x=170,y=150)
category_options=['business','entertainment','general','health','science','sports','technology']
category_label=Label(news_frame, text = 'Select Category',font=helv36,fg="white",bg='#999966')
category_label.place(x=10,y=224)
category_combo = ttk.Combobox(news_frame, value=category_options,font=helv36,width=12)
category_combo.current(0)
category_combo.place(x=180,y=224)
query_label=Label(news_frame, text = 'Search For:',font=helv36,fg="white",bg='#999966')
query_label.place(x=10,y=298)
query_entry= Entry(news_frame,width=20,font=helv36)
query_entry.place(x=140,y=298)
bring_news_button = Button(news_frame,text='Filter News',width=20,height=1,fg='white',border=0,bg='#999966',command=bring_news)
bring_news_button['font']=helv36
bring_news_button.place(x=70,y=335)    

counter = time.ctime()[:19].replace(':','_')

open_weather = json.load(open('open_weather.json'))

weather_frame = Frame(root,width=450, height=550,bg='#66ccff')
weather_city_name_label = Label(weather_frame, text = 'Enter City Name',font=helv36,fg="white",bg='#66ccff')
weather_city_name_label.place(x=10,y=224)
weather_city_name_entry = Entry(weather_frame,width=20,font=helv36)
weather_city_name_entry.place(x=180,y=224)
weather_sub_btn=Button(weather_frame,text='Click me',width=20,height=1,fg='white',border=0,bg='#66ccff',command=submit)
weather_sub_btn['font']=helv36
weather_sub_btn.place(x=120,y=261) 

bitcoin_frame = Frame(root, width=450, height=550,bg='#ff704d')
bitcoin_btn=Button(bitcoin_frame,text='Click For The BitCoin Info',width=20,height=1,fg='white',border=0,bg='#ff704d',command=bc)
bitcoin_btn['font']=helv36
bitcoin_btn.place(x=90,y=224)

currency_frame = Frame(root, width=450, height=550,bg='#4dff4d')
currency_btn=Button(currency_frame,text = 'Click For The Currency Info', command = cr,width=24,height=1,fg='white',border=0,bg='#4dff4d')
currency_btn['font']=helv36
currency_btn.place(x=90,y=224)

horoscope_frame = Frame(root, width=450, height=550,bg='#ff8533')
horoscope_label = Label(horoscope_frame, text = 'Get Daily Horoscope Info: ',font=helv36, fg="white",bg='#ff8533')
horoscope_label.place(x=10,y=190)
horoscopes=['aries','taurus','gemini','cancer','leo','virgo','libra',
'scorpio','sagittarius','capricorn','aquarius','pisces']
horoscope_combo = ttk.Combobox(horoscope_frame, value=horoscopes,font=helv36,width=10)
horoscope_combo.current(0)
horoscope_combo.place(x=280,y=190)
horoscope_btn=Button(horoscope_frame,text = 'Click For The Daily Horoscope Info', command = hr,width=28,height=1,fg='white',border=0,bg='#ff8533')
horoscope_btn['font']=helv36
horoscope_btn.place(x=40,y=261) 


helv37 = font.Font(family='Helvetica',size=20, weight='bold')
main=Button(root,text='M E N U',command=main_menu,border=0,bg='#262626',fg='#666699',activeforeground='#12c4c0',activebackground='#262626')
#
main['font']=helv37
main.place(x=5,y=10)

root.mainloop()