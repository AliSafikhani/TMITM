from django.shortcuts import render, redirect,get_object_or_404
from django.db import connection
from django.views.decorators.csrf import csrf_exempt , csrf_protect
from django.db.models import Q
from .models import Transformer
from .forms import TransformerForm
from django.core.files.storage import FileSystemStorage

# index FUNCTION 
#.....................................................................................
#.....................................................................................
def index(request):
    return render(request, 'index.html')

# transformer_spec FUNCTION 
#.....................................................................................
#.....................................................................................

def transformer_spec(request):
    return render(request, 'transformer_spec.html')


# add_transformer FUNCTION 
#.....................................................................................
#.....................................................................................

def add_transformer(request):
    if request.method == 'POST':
        name = request.POST['name']
        voltage = request.POST['voltage']
        location = request.POST['location']
        manufacturer = request.POST['manufacturer']
        operation_year = request.POST['operation_year']
        image = request.FILES['image']

        print("image.name:", image.name)  # Debug print

        # Save the image to the filesystem
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)
        print("image_url:", image_url)  # Debug print


        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO transformersa (name, voltage, location, manufacturer, operation_year, image_url) VALUES (%s,%s, %s, %s, %s, %s)',
                [name, voltage, location, manufacturer, operation_year, image_url])
        
        return redirect('/')
    
    return render(request, 'transformer_spec.html')


# test FUNCTION 
#.....................................................................................
#.....................................................................................

@csrf_exempt
def test(request):
    return render(request, 'test.html')


# add FUNCTION 
#.....................................................................................
#.....................................................................................

def add(request):
    return render(request, 'add.html')

# search FUNCTION 
#.....................................................................................
#.....................................................................................


@csrf_exempt
def search(request):
    query = request.GET.get('query', '')
    print("query:",query)  # Debug print


    with connection.cursor() as cursor:
        sql_query = '''
            SELECT * FROM transformersa 
            WHERE name LIKE %s 
            OR voltage LIKE %s 
            OR location LIKE %s 
            OR manufacturer LIKE %s
            OR operation_year LIKE %s
        '''
        name = request.POST['name']
        voltage = request.POST['voltage']
        location = request.POST['location']
        manufacturer = request.POST['manufacturer']
        operation_year= request.POST['operation_year']
        params =[name, voltage, location, manufacturer, operation_year]
        

        cursor.execute(sql_query, params)
        results = cursor.fetchall()

        print("Query Results:", voltage)  # Debug print

        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in results]
        for transformer in results:
            print("Query Results:",transformer)  # Debug print

    return render(request, 'search.html', {'results': results, 'query': query})

# edit_transformer FUNCTION 
#.....................................................................................
#.....................................................................................

@csrf_protect
def edit_transformer(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        voltage = request.POST.get('voltage')
        location = request.POST.get('location')
        manufacturer = request.POST.get('manufacturer')
        operation_year= request.POST.get('operation_year')
        image = request.FILES.get('image')
        with connection.cursor() as cursor:
            cursor.execute('UPDATE transformersa SET name=%s, voltage=%s, location=%s, manufacturer=%s , operation_year=%s WHERE id=%s',
                           [name, voltage, location, manufacturer,operation_year, id])
        return render(request, 'transformer_spec.html')


    else:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM transformersa WHERE id=%s', [id])
            transformer = cursor.fetchone()
            if not transformer:
                return redirect('search')

            columns = [col[0] for col in cursor.description]
            transformer = dict(zip(columns, transformer))

        return render(request, 'edit.html', {'transformer': transformer})

# delete_transformer FUNCTION 
#.....................................................................................
#.....................................................................................

@csrf_protect
def delete_transformer(request, id):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM transformersa WHERE id = %s', [id])
    return render(request, 'transformer_spec.html')


# show FUNCTION 
#.....................................................................................
#.....................................................................................

@csrf_exempt
def show(request):
    query = request.GET.get('query', '')

    with connection.cursor() as cursor:
        sql_query = '''
            SELECT * FROM transformersa 
        '''
        cursor.execute(sql_query)
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in results]

    return render(request, 'show.html', {'results': results, 'query': query})


# dga FUNCTION 
#.....................................................................................
#.....................................................................................


def dga(request):
    return render(request, 'dga.html')

# dga_resaults FUNCTION 
#.....................................................................................
#.....................................................................................


def dga_resaults(request):
    return render(request, 'dga_resaults.html')

# dga_resaults FUNCTION 
#.....................................................................................
#.....................................................................................
def doal(request):
    return render(request, 'doal.html')

# fra FUNCTION 
#.....................................................................................
#.....................................................................................
from .plot_generator import PlotGenerator
def doal_resault(request):
    plot_gen = PlotGenerator()
    otpt= plot_gen.generate_plot(request)
    serial_number=otpt[0]
    graph1=otpt[1]
    graph2=otpt[2]
    graph3=otpt[3]

    return render(request, 'doal_resault.html', {'serial_number': serial_number,'graph1': graph1, 'graph2': graph2, 'graph3': graph3})

# fra FUNCTION 
#.....................................................................................
#.....................................................................................


def fra(request):
    return render(request, 'fra.html')

# resistance FUNCTION 
#.....................................................................................
#.....................................................................................


def resistance(request):
    return render(request, 'resistance.html')

# tan_delta FUNCTION 
#.....................................................................................
#.....................................................................................


def tan_delta(request):
    return render(request, 'tan_delta.html')

# add_dga_test_resaults FUNCTION 
#.....................................................................................
#.....................................................................................


def add_dga_test_resaults(request):
    return render(request, 'add_dga_test_resaults.html')

# dga_gas_adding FUNCTION 
#.....................................................................................
#.....................................................................................

def dga_gas_adding(request):
    if request.method == 'POST':
        serial_number = request.POST['sn']
        # labratury = request.POST('lab')
        # methodoftest = request.POST('mot')
        print(serial_number)
        request.session['serial_number'] = serial_number

        with connection.cursor() as cursor:
            cursor.execute (f'CREATE TABLE IF NOT EXISTS  TFR{serial_number} (hydrogen int(255), oxygen int(255) ,nitrogen int(255) ,carbon_monoxide int(255),carbon_dioxide int(255),methane int(255),ethylene int(255),ethane int(255),acetylene int(255),propene int(255),propane int(255))') 
        # return redirect('/')
    return render(request, 'dga_gas_adding.html')

# dga_gas_adding_dga FUNCTION 
#.....................................................................................
#.....................................................................................

def dga_gas_adding_dga(request):
    serial_number = request.session.get('serial_number')
    sn= f'tfr{serial_number}'
    # tn=f'tfr{serial_number}'
    if request.method == 'POST':
        hydrogen = request.POST['hydrogen']
        oxygen = request.POST['oxygen'] 
        nitrogen = request.POST['nitrogen']
        carbon_monoxide = request.POST['carbon_monoxide']
        carbon_dioxide= request.POST['carbon_dioxide']
        methane = request.POST['methane']
        ethylene = request.POST['ethylene']
        ethane = request.POST['ethane']
        acetylene = request.POST['acetylene']
        propene = request.POST['propene']
        propane = request.POST['propane'] 

        with connection.cursor() as cursor:
            cursor.execute(f'INSERT INTO {sn} (hydrogen,oxygen,nitrogen,carbon_monoxide,carbon_dioxide,methane,ethylene,ethane,acetylene,propene,propane) VALUES (%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s)',
                [hydrogen,oxygen,nitrogen,carbon_monoxide,carbon_dioxide,methane,ethylene,ethane,acetylene,propene,propane])
        
        return redirect('/')
    
    return render(request, 'transformer_spec.html')

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import TimeSeriesData
import urllib.parse

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('plot_data')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    lines = f.read().decode('utf-8').splitlines()
    for line in lines[1:]:  # Skip header row
        row = line.split(',')
        TimeSeriesData.objects.create(
            timestamp_r=float(row[0]), value_r=float(row[1]),
            timestamp_s=float(row[2]), value_s=float(row[3]),
            timestamp_t=float(row[4]), value_t=float(row[5])
        )

def plot_data(request):
    data = TimeSeriesData.objects.all()
    times_r = [d.timestamp_r for d in data]
    values_r = [d.value_r for d in data]
    times_s = [d.timestamp_s for d in data]
    values_s = [d.value_s for d in data]
    times_t = [d.timestamp_t for d in data]
    values_t = [d.value_t for d in data]

    plt.figure(figsize=(10, 18))
    
    plt.subplot(3, 1, 1)
    plt.plot(times_r, values_r)
    plt.xlabel('Time (s)')
    plt.ylabel('R (V)')
    plt.title('Time Series Data R')
    
    plt.subplot(3, 1, 2)
    plt.plot(times_s, values_s)
    plt.xlabel('Time (s)')
    plt.ylabel('S (V)')
    plt.title('Time Series Data S')
    
    plt.subplot(3, 1, 3)
    plt.plot(times_t, values_t)
    plt.xlabel('Time (s)')
    plt.ylabel('T (V)')
    plt.title('Time Series Data T')    

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    # uri = 'data:image/png;base64,'
    return render(request, 'plott.html', {'data': uri})

# this is the test for git 
     




