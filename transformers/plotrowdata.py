import matplotlib.pyplot as plt
from io import BytesIO
import base64
import io
from .models import TimeSeriesData
from .forms import FileUploadForm
import urllib.parse
from django.shortcuts import render, redirect


def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('plott')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    TimeSeriesData.objects.all().delete()
    lines = f.read().decode('utf-8').splitlines()
    for line in lines[1:]:  # Skip header row
        row = line.split(',')
        TimeSeriesData.objects.create(
            timestamp_r=float(row[0]), value_r=float(row[1]),
            timestamp_s=float(row[2]), value_s=float(row[3]),
            timestamp_t=float(row[4]), value_t=float(row[5])
        )
class plotrowdata:
    def plottf(self,request):
        data = TimeSeriesData.objects.all()
        times_r = [d.timestamp_r for d in data]
        values_r = [d.value_r for d in data]
        times_s = [d.timestamp_s for d in data]
        values_s = [d.value_s for d in data]
        times_t = [d.timestamp_t for d in data]
        values_t = [d.value_t for d in data]

        plt.figure(figsize=(7, 15))
        fig1=plt.figure()
        # plt.subplot(3, 1, 1)
        plt.plot(times_r, values_r)
        plt.xlabel('Time (s)')
        plt.ylabel('R (V)')
        plt.title('Time Series Data R')
        test1= self._convert_plot_to_base64(fig1)
        fig2=plt.figure()
        # plt.subplot(3, 1, 2)
        plt.plot(times_s, values_s)
        plt.xlabel('Time (s)')
        plt.ylabel('S (V)')
        plt.title('Time Series Data S')
        test2= self._convert_plot_to_base64(fig2)
        fig3=plt.figure()
        # plt.subplot(3, 1, 3)
        plt.plot(times_t, values_t)
        plt.xlabel('Time (s)')
        plt.ylabel('T (V)')
        plt.title('Time Series Data T')
        test3= self._convert_plot_to_base64(fig3)    

        # buf = BytesIO()
        # plt.savefig(buf, format='png')
        # buf.seek(0)
        # string = base64.b64encode(buf.read())
        # uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        return(test1,test2,test3)

    def _convert_plot_to_base64(self, fig):
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        plt.close(fig)
        return base64.b64encode(image_png).decode('utf-8')
