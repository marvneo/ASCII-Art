from PIL import Image



def main():

    file_name = input('This program turns a photo into ASCII art. Please type file name: ')
    image = Image.open(file_name)

    pix_list = list(image.getdata())
    width, height = image.size

    RGB_matrix = get_RGB_matrix(pix_list,width,height)
    intensity_matrix = get_intensity_matrix(RGB_matrix)
    print_ASCII(intensity_matrix)



def get_RGB_matrix(pix_list, width, height):
    RGB_matrix = []
    count = 0

    while count < len(pix_list):
        for i in range(height):
            row = []
            for j in range(width):
                row.append(pix_list[count])
                count+=1
            RGB_matrix.append(row)

    return RGB_matrix



def get_intensity_matrix(RGB_matrix):

    brightness_matrix = []

    for row in RGB_matrix:
        temp = []
        for col in row:
            temp.append((col[0]*0.2126+col[1]*0.7152+col[2]*0.0722))
        brightness_matrix.append(temp)
    
    return brightness_matrix



def print_ASCII(intensity_matrix):
    ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{/}[]?-_+~<>i!lI;:,^`'. "
    output = []

    for row in intensity_matrix:
        temp = []
        for col in row:
            #print(round(col/3.695))
            temp.append(ascii[round((len(ascii)-col)/3.695)])
        output.append(temp)

    for row in output:
        line = [i+i+i for i in row]
        print("".join(line))

main()