def jpeg_res(filename):

    with open(filename, 'rb') as myfile:

        myfile.seek(163)

        a = myfile.read(2)

        height = (a[0] << 8) + a[1]

        a = myfile.read(2)

        width = (a[0] << 8) + a[1]

    print("The resolution of the image is: {} x {}".format(height, width))

resolution = jpeg_res("psychedelic.jpg")
