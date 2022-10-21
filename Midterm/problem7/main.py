import easy_a_star
import djikstra
# import rrt_star
import bidirectional_a_star
import breadth_first_search
import a_star


def main():
    print("#### Bidirectional A* ####")
    bidirectional_a_star.main()

    print("#### A* ####")
    a_star.main()

    print("#### Easy A* ####")
    easy_a_star.main()

    print("#### Djikstra ####")
    djikstra.main()

    # print("#### RRT* ####")
    # rrt_star.main()

    print("#### Breadth First Search ####")
    breadth_first_search.main()

    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # start = (0, 0)
    # end = (7, 6)

    # path = easy_a_star.astar(maze, start, end)
    # print(path)


if __name__ == '__main__':
    main()