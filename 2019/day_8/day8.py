

def get_image(fileName):
    Input = open('day_1_input', 'r')
    image = list(Input.readlines()[0])
    n = len(image)
    return image, n

def get_img_size():
    return 25, 6

def part1():
    image, n = get_image('day_1_input') 
    width, high = get_img_size()
    layerSize = width * high

    min0 = 999999
    maxLayer = 0
    count = 0
    for i in range(n):
        # count the 0s from each layer
        if image[i] == '0':
            count += 1
        # keep the layer with fewest 0s
        if (i + 1) % layerSize == 0:
            if min0 > count:
                maxLayer = i // layerSize
                min0 = count
            count = 0
    
    count_1 = 0
    count_2 = 0
    start = maxLayer * layerSize 
    end = start + layerSize
    # count 1 and 2 from the layer
    # with the fewest 0s
    for i in range(start, end):
        if image[i] == '1':
            count_1 += 1
        if image[i] == '2':
            count_2 += 1

    print("1 digits ", count_1)
    print("2 digits ", count_2)
    print("1 x 2 digits ", count_1 * count_2)


def part2():
    image, n = get_image('input_2')
    width, high = get_img_size()
    layerSize = width * high
    layerCount = n // layerSize

    # decode the image
    for i in range(layerSize):
        for j in range(layerCount):
            idx = j * layerSize + i
            if image[idx] == '0':
                image[i] = '0'
                break
            if image[idx] == '1':
                image[i] = '1'
                break
    
    # print the decoded image
    for i in range(high):
        for j in range(width):
            if image[i * width + j] == '1':
                print(image[i * width + j], end="")
            else:
                print(" ", end="")
        print("")


part1()
part2()