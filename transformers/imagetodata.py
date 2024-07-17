import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"File not found: {image_path}")
        return image
    except Exception as e:
        print(e)
        return None

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    return edges

def detect_lines(edges):
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    return lines

def extract_points(lines):
    x_vals = []
    y_vals = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        x_vals.extend([x1, x2])
        y_vals.extend([y1, y2])
    return sorted(x_vals), sorted(y_vals, reverse=True)

def plot_detected_points(image, lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    plt.figure(figsize=(10, 5))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Detected Points')
    plt.show()

def main(image_path):
    image = load_image(image_path)
    if image is not None:
        edges = preprocess_image(image)
        lines = detect_lines(edges)
        if lines is not None:
            x_vals, y_vals = extract_points(lines)
            plot_detected_points(image, lines)
            print("X Values:", x_vals)
            print("Y Values:", y_vals)
        else:
            print("No lines detected.")
    else:
        print("Failed to load image.")

if __name__ == "__main__":
    image_path = 'aaa.png'
    main(image_path)
