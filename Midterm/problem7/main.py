import easy_a_star
import djikstra
import rrt_star
import bidirectional_a_star
import breadth_first_search
import a_star


def main():

    print("#### Easy A* ####")
    easy_a_star.main()

    print("#### Bidirectional A* ####")
    bidirectional_a_star.main()

    print("#### A* ####")
    a_star.main()

    print("#### Djikstra ####")
    djikstra.main()

    print("#### RRT* ####")
    rrt_star.main()

    print("#### Breadth First Search ####")
    breadth_first_search.main()


if __name__ == '__main__':
    main()