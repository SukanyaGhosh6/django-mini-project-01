from django.shortcuts import render


# Create your views here.
# CONTEXT -- It is used to send the data from backend to frontend
data = [
    {
        'id': 1,
        'name': 'Trisha',
        'loc': 'Andhra Pradesh',
        'desc':'Andhra Pradesh is a coastal state in southeastern India known for its rich cultural heritage, historical temples, and delicious cuisine. It is also a major hub for agriculture, film production (Tollywood), and rapidly growing industries.'
    },
    {
        'id': 2,
        'name':'Dhrubajyoti',
        'loc': 'Kolkata',
        'desc':'Kolkata, the capital of West Bengal, is a vibrant city known for its colonial architecture, literary heritage, and cultural festivals like Durga Puja. It is also a major commercial, educational, and artistic center in eastern India.'
    },
    {
        'id': 3,
        'name':'Aakash',
        'loc': 'Tamil Nadu',
        'desc':'Tamil Nadu, located in southern India, is renowned for its ancient temples, classical arts, and rich Dravidian culture. It is also a leading state in industries, education, and technology, with Chennai as its capital.'
    },
    {
        'id': 4,
        'name':'Ashish',
        'loc': 'Surat',
        'desc':'Surat, located in Gujarat, is a rapidly growing city known for its diamond polishing and textile industries. It is one of India’s cleanest cities and a major hub of commerce and trade in western India.'
    },
    {
        'id': 5,
        'name':'Sukanya',
        'loc': 'Assam',
        'desc':'Assam, located in northeastern India, is famous for its tea plantations, rich biodiversity, and the mighty Brahmaputra River. It is also known for its unique culture, traditional Bihu dance, and lush green landscapes.'
    },

]

#context ---- it is always passed in the form of dictionary

def home(request):
    return render(request,'home.html',{'sakshi': data})

def read(request,pk):
    for i in data:
        if i['id'] == pk:
            context = {'trainer':i} #var[key]--->value
    return render(request,'read.html',context)
