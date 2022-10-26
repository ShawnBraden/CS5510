import easy_a_star
import djikstra
import rrt_star
import bidirectional_a_star
import breadth_first_search
import a_star
import matplotlib.pyplot as plt

algorithmNames = ["Easy A*", "A*", "Bidir A*", "Djikstra", "RRT*", "BFS"]
distance = []
time = []

def main():
    print("#### Easy A* ####")
    easyAStar = easy_a_star.main()
    distance.append(easyAStar[0])
    time.append(easyAStar[1])
    
    print("#### A* ####")
    aStar = a_star.main()
    distance.append(aStar[0])
    time.append(aStar[1])

    print("#### Bidirectional A* ####")
    biAStar = bidirectional_a_star.main()
    distance.append(biAStar[0])
    time.append(biAStar[1])

    print("#### Djikstra ####")
    djik = djikstra.main()
    distance.append(djik[0])
    time.append(djik[1])

    print("#### RRT* ####")
    rrt = rrt_star.main()
    distance.append(rrt[0])
    time.append(rrt[1])

    print("#### Breadth First Search ####")
    bfs = breadth_first_search.main()
    distance.append(bfs[0])
    time.append(bfs[1])

    # graph distance
    plt.bar(algorithmNames, distance)
    plt.title('Distance Comparison')
    plt.xlabel('Algorithms')
    plt.ylabel('Average Distance (m)')
    plt.show()

    # graph time
    plt.bar(algorithmNames, time)
    plt.title('Time Comparison')
    plt.xlabel('Algorithms')
    plt.ylabel('Average Time (ms)')
    plt.show()

if __name__ == '__main__':
    main()