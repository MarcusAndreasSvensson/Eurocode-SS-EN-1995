def beräkna_area(polygon):
    area = 0

    i = 0
    for _ in polygon:
        try:
            area += (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1])
            i += 1
        except IndexError:
            area += (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1])
            break

    area = abs(area) * 1/2

    return area


def beräkna_centroid(polygon):
    centroid_x = 0
    centroid_y = 0

    i = 0
    for _ in polygon:
        try:
            centroid_x += ((polygon[i][0] + polygon[i+1][0]) * (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]))
            centroid_y += ((polygon[i][1] + polygon[i+1][1]) * (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]))
            i += 1
        except IndexError:
            centroid_x += ((polygon[i][0] + polygon[0][0]) * (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]))
            centroid_y += ((polygon[i][1] + polygon[0][1]) * (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]))
            break

    area = beräkna_area(polygon)
    centroid_x = abs(centroid_x) * 1/(6*area)
    centroid_y = abs(centroid_y) * 1/(6*area)

    centroids = [centroid_x, centroid_y]

    return centroids


def beräkna_tröghetsmoment(polygon):
    I_x = 0
    I_y = 0
    centroid = beräkna_centroid(polygon)

    i = 0
    for _ in polygon:
        try:
            area = polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]

            x = pow((polygon[i][1] - centroid[1]), 2) + (polygon[i][1] - centroid[1]) * (polygon[i+1][1] - centroid[1]) + pow((polygon[i+1][1] - centroid[1]), 2)
            y = pow((polygon[i][0] - centroid[0]), 2) + (polygon[i][0] - centroid[0]) * (polygon[i+1][0] - centroid[0]) + pow((polygon[i+1][0] - centroid[0]), 2)

            I_x += x * area
            I_y += y * area

            i += 1

        except IndexError:
            area = polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]

            x = pow((polygon[i][1] - centroid[1]), 2) + (polygon[i][1] - centroid[1]) * (polygon[0][1] - centroid[1]) + pow((polygon[0][1] - centroid[1]), 2)
            y = pow((polygon[i][0] - centroid[0]), 2) + (polygon[i][0] - centroid[0]) * (polygon[0][0] - centroid[0]) + pow((polygon[0][0] - centroid[0]), 2)

            I_x += x * area
            I_y += y * area

            break

    I_x = abs(I_x) / 12
    I_y = abs(I_y) / 12

    #test_x = 2 * (100 * pow(10, 3) / 12) + 2 * 100 * 10 * pow(45, 2) + (20 * pow(80, 3) / 12)
    #test_y = 2 * (10 * pow(100, 3) / 12) + (80 * pow(20, 3) / 12)

    I = [I_x, I_y]

    return I


if __name__ == "__main__":
    poly = [[0,0], [0,10], [40,10], [40,90], [0,90], [0,100],
            [100,100], [100,90], [60,90], [60,10], [100, 10], [100,0]]
    j = 0
    for _ in poly:
        poly[j][0] += 10
        poly[j][1] += 10
        j += 1

    print(poly)

    poly_2 = [(0,0), (0,2), (2,2), (2,0)]

    poly_3 = [(2,2), (2,4), (4,4), (4,2)]



    print("area:", beräkna_area(poly_2))

    hej = beräkna_centroid(poly_2)
    print("centroid:", hej)

    I = beräkna_tröghetsmoment(poly_2)
    print("tröghetsmoment:", I)