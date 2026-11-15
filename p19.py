import cv2
import matplotlib.pyplot as plt

# 1. Load the image from the original_images folder
image = cv2.imread('original_images/example.jpg')

if image is None:
    print("Error: Image not found! Make sure 'example.jpg' is inside the 'original_images' folder.")
else:
    # Get image dimensions
    height, width, _ = image.shape

    # 2. Define start and end points for the bi-directional arrows
    arrow_start_left = (20, height - 50)          # Left starting point
    arrow_end_right = (width - 20, height - 50)   # Right end point

    # Draw arrows in both directions (using BGR color format for OpenCV: Blue=(255, 0, 0), Red=(0, 0, 255))
    cv2.arrowedLine(image, arrow_start_left, arrow_end_right, (0, 0, 255), 3, tipLength=0.05)  # Rightward arrow
    cv2.arrowedLine(image, arrow_end_right, arrow_start_left, (0, 0, 255), 3, tipLength=0.05)  # Leftward arrow

    # 3. Annotate the width value dynamically at the midpoint above the arrows
    width_label_position = (width // 2 - 100, height - 80)
    cv2.putText(
        image,
        f'Width: {width} px',
        width_label_position,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # 4. Save the annotated image in the output_images folder
    cv2.imwrite('output_images/annotated_width.jpg', image)
    print("Annotated image saved successfully to 'output_images/annotated_width.jpg'!")

    # Convert BGR to RGB to display properly with Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Annotated Image with Bi-Directional Width Arrows")
    plt.axis('off')
    plt.show()