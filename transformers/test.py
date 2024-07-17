
# plot_generator.py

import matplotlib.pyplot as plt
import io
import base64

class PlotGenerator:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def generate_plot1(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3], label=f"Transformer {self.serial_number} - Plot 1")
        ax.legend()
        return self._convert_plot_to_base64(fig)

    def generate_plot2(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [4, 3, 2, 1], label=f"Transformer {self.serial_number} - Plot 2")
        ax.legend()
        return self._convert_plot_to_base64(fig)

    def generate_plot3(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [2, 2, 2, 2], label=f"Transformer {self.serial_number} - Plot 3")
        ax.legend()
        return self._convert_plot_to_base64(fig)

    def _convert_plot_to_base64(self, fig):
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        plt.close(fig)
        return base64.b64encode(image_png).decode('utf-8')
