from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


def main():
    file = open("mug.off", "r")
    edges, faces = read_off(file)

    fig = pyplot.figure()
    axes3D = Axes3D(fig)
    for i in range(len(edges)):
        axes3D.scatter(edges[i][0], edges[i][1], edges[i][2])

    pyplot.savefig('result.png')
    print('\"result.png\" is saved successfully!')

    pyplot.show()


# noinspection PyUnusedLocal
def read_off(file):
    if 'OFF' != file.readline().strip():
        raise Exception('Not a valid OFF header')
    n_edges, n_faces, n_dont_know = tuple([int(s) for s in file.readline().strip().split(' ')])
    edges = [[float(s) for s in file.readline().strip().split(' ')] for i_edge in range(n_edges)]
    faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
    return edges, faces


if __name__ == "__main__":
    main()
