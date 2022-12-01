import java.io.*;
import java.util.*;

public class homework {
    // output property
    private static int cost = 0;
    private static boolean success = false;
    private static int stepNum = 0;
    private static int[][] steps = new int[0][];

    public static void main(String[] args) {
        // BFS:1, UCS:2, A*:3
        int searchType = 0;
        int[] entrance = new int[3];
        int[] exit = new int[3];
        // int availableNodeCount = 0;
        // array for available action
        Node[][][] array = new Node[0][][];

        //Read file and construct array
        try {
            BufferedReader in = new BufferedReader(new FileReader("input.txt"));
            String str;
            int lineCount = 0;
            while ((str = in.readLine()) != null && lineCount < 4) {
                if (lineCount == 0) {
                    // determine search type
                    switch (str) {
                        case "BFS":
                            searchType = 1;
                            break;
                        case "UCS":
                            searchType = 2;
                            break;
                        case "A*":
                            searchType = 3;
                            break;
                    }
                } else if (lineCount == 1) {
                    // build empty nodes array
                    String[] dimensionArray = str.split(" ");
                    array = new Node[Integer.parseInt(dimensionArray[0])][Integer.parseInt(dimensionArray[1])][Integer.parseInt(dimensionArray[2])];
                } else if (lineCount == 2) {
                    String[] entranceArray = str.split(" ");
                    entrance[0] = Integer.parseInt(entranceArray[0]);
                    entrance[1] = Integer.parseInt(entranceArray[1]);
                    entrance[2] = Integer.parseInt(entranceArray[2]);
                } else if (lineCount == 3) {
                    String[] exitArray = str.split(" ");
                    exit[0] = Integer.parseInt(exitArray[0]);
                    exit[1] = Integer.parseInt(exitArray[1]);
                    exit[2] = Integer.parseInt(exitArray[2]);
                }
                lineCount++;
            }
            // availableNodeCount = Integer.parseInt(str);
            while ((str = in.readLine()) != null) {
                String[] dimensionActionArray = str.split(" ");
                int[] act = new int[dimensionActionArray.length - 3];
                for (int i = 3; i < dimensionActionArray.length; i++) {
                    act[i - 3] = Integer.parseInt(dimensionActionArray[i]);
                }
                array[Integer.parseInt(dimensionActionArray[0])]
                        [Integer.parseInt(dimensionActionArray[1])]
                        [Integer.parseInt(dimensionActionArray[2])] = new Node();
                array[Integer.parseInt(dimensionActionArray[0])]
                        [Integer.parseInt(dimensionActionArray[1])]
                        [Integer.parseInt(dimensionActionArray[2])].action = act;

            }
        } catch (IOException e) {
        }

        if (searchType == 1) {
            // System.out.println("BFS");
            BFS(array, entrance, exit);
        } else if (searchType == 2) {
            // System.out.println("UCS");
            UCS(array, entrance, exit);
        } else if (searchType == 3) {
            // System.out.println("AStar");
            AStar(array, entrance, exit);
        }

    }

    static boolean arrayIsEqual(int[] a, int[] b) {
        if (a.length != b.length) return false;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    static private void BFS(Node[][][] array, int[] entrance, int[] exit) {
        Node entranceNode = array[entrance[0]][entrance[1]][entrance[2]];
        entranceNode.cost = 0;
        entranceNode.visited = true;

        // ensure there is a node in exit coordinate
        if (array[exit[0]][exit[1]][exit[2]] == null) {
            array[exit[0]][exit[1]][exit[2]] = new Node();
        }

        Deque<int[]> queue = new LinkedList<>();
        queue.addFirst(entrance);
        while (!queue.isEmpty() && !success) {
            int[] curCoordinate = queue.removeFirst();
            Node curNode = array[curCoordinate[0]][curCoordinate[1]][curCoordinate[2]];
            for (int i = 0; i < curNode.action.length; i++) {
                int[] nextCoordinate = takeAction(curNode.action[i], (int[]) Arrays.copyOf(curCoordinate, 3));
                if (array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]] != null && array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]].visited == false) {
                    if (arrayIsEqual(nextCoordinate, exit)) {
                        success = true;
                    }
                    Node nextNode = array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]];
                    nextNode.stepCost = 1;
                    nextNode.cost = curNode.cost + nextNode.stepCost;
                    nextNode.pre = curCoordinate;
                    nextNode.visited = true;
                    queue.addLast(nextCoordinate);
                }
            }
        }
        createOutput(array, entrance, exit);

    }

    static private void UCS(Node[][][] array, int[] entrance, int[] exit) {
        Node entranceNode = array[entrance[0]][entrance[1]][entrance[2]];
        entranceNode.cost = 0;
        entranceNode.visited = true;

        // ensure there is a node in exit coordinate
        if (array[exit[0]][exit[1]][exit[2]] == null) {
            array[exit[0]][exit[1]][exit[2]] = new Node();
        }

        Comparator<int[]> cmp = new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return array[a[0]][a[1]][a[2]].cost - array[b[0]][b[1]][b[2]].cost;
            }
        };

        Queue<int[]> queue = new PriorityQueue<>(cmp);

        queue.add(entrance);
        while (!queue.isEmpty() && !success) {
            int[] curCoordinate = queue.remove();
            Node curNode = array[curCoordinate[0]][curCoordinate[1]][curCoordinate[2]];
            for (int i = 0; i < curNode.action.length; i++) {
                int[] nextCoordinate = takeAction(curNode.action[i], (int[]) Arrays.copyOf(curCoordinate, 3));
                if (array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]] != null && array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]].visited == false) {
                    if (arrayIsEqual(nextCoordinate, exit)) {
                        success = true;
                    }
                    Node nextNode = array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]];
                    if (curNode.action[i] <= 6) {
                        nextNode.stepCost = 10;
                    } else {
                        nextNode.stepCost = 14;
                    }
                    nextNode.cost = curNode.cost + nextNode.stepCost;
                    nextNode.pre = curCoordinate;
                    nextNode.visited = true;
                    queue.add(nextCoordinate);
                }
            }
        }
        createOutput(array, entrance, exit);
    }

    static private int getHeuristic(int[] a, int[] b) {
        int xDisSqr = (int) Math.pow((a[0] - b[0]), 2);
        int yDisSqr = (int) Math.pow((a[1] - b[1]), 2);
        int zDisSqr = (int) Math.pow((a[2] - b[2]), 2);
        return (int) Math.sqrt(xDisSqr + yDisSqr + zDisSqr);
    }

    static private void AStar(Node[][][] array, int[] entrance, int[] exit) {
        Node entranceNode = array[entrance[0]][entrance[1]][entrance[2]];
        entranceNode.cost = 0;
        entranceNode.visited = true;

        // ensure there is a node in exit coordinate
        if (array[exit[0]][exit[1]][exit[2]] == null) {
            array[exit[0]][exit[1]][exit[2]] = new Node();
        }

        Comparator<int[]> cmp = new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                int fA = array[a[0]][a[1]][a[2]].cost + getHeuristic(a, exit);
                int fB = array[b[0]][b[1]][b[2]].cost + getHeuristic(b, exit);
                return fA - fB;
            }
        };

        Queue<int[]> queue = new PriorityQueue<>(cmp);

        queue.add(entrance);
        while (!queue.isEmpty() && !success) {
            int[] curCoordinate = queue.remove();
            Node curNode = array[curCoordinate[0]][curCoordinate[1]][curCoordinate[2]];
            for (int i = 0; i < curNode.action.length; i++) {
                int[] nextCoordinate = takeAction(curNode.action[i], (int[]) Arrays.copyOf(curCoordinate, 3));
                if (array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]] != null && array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]].visited == false) {
                    if (arrayIsEqual(nextCoordinate, exit)) {
                        success = true;
                    }
                    Node nextNode = array[nextCoordinate[0]][nextCoordinate[1]][nextCoordinate[2]];
                    if (curNode.action[i] <= 6) {
                        nextNode.stepCost = 10;
                    } else {
                        nextNode.stepCost = 14;
                    }
                    nextNode.cost = curNode.cost + nextNode.stepCost;
                    nextNode.pre = curCoordinate;
                    nextNode.visited = true;
                    queue.add(nextCoordinate);
                }
            }
        }
        createOutput(array, entrance, exit);
    }

    static private void createOutput(Node[][][] array, int entrance[], int exit[]) {
        if (success == false) {
            try {
                BufferedWriter out = new BufferedWriter(new FileWriter("output.txt"));
                out.write("FAIL");
                out.close();
            } catch (IOException e) {
                //
            }
            return;
        }
        Node exitNode = array[exit[0]][exit[1]][exit[2]];
        int totalCost = exitNode.cost;
        Deque<int[]> steps = new LinkedList<>();
        steps.addFirst(new int[]{exit[0], exit[1], exit[2], exitNode.stepCost});
        int[] pre = exitNode.pre;
        while (!arrayIsEqual(pre, entrance)) {
            Node preNode = array[pre[0]][pre[1]][pre[2]];
            steps.addFirst(new int[]{pre[0], pre[1], pre[2], preNode.stepCost});
            pre = preNode.pre;
        }
        steps.addFirst(new int[]{pre[0], pre[1], pre[2], 0});

        //write data
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter("output.txt"));
            out.write(totalCost + "\n");
            out.write(steps.size() + "\n");
            int count = 0;
            for (int[] step : steps) {
                if (count != steps.size() - 1) {
                    out.write(step[0] + " " + step[1] + " " + step[2] + " " + step[3] + "\n");
                } else {
                    out.write(step[0] + " " + step[1] + " " + step[2] + " " + step[3]);
                }
                count++;
            }
            out.close();
        } catch (IOException e) {
            //
        }
    }

    // obtain new coordinate by action
    static private int[] takeAction(int act, int[] coordinate) {
        switch (act) {
            case 1:
                coordinate[0] += 1;
                break;
            case 2:
                coordinate[0] -= 1;
                break;
            case 3:
                coordinate[1] += 1;
                break;
            case 4:
                coordinate[1] -= 1;
                break;
            case 5:
                coordinate[2] += 1;
                break;
            case 6:
                coordinate[2] -= 1;
                break;
            case 7:
                coordinate[0] += 1;
                coordinate[1] += 1;
                break;
            case 8:
                coordinate[0] += 1;
                coordinate[1] -= 1;
                break;
            case 9:
                coordinate[0] -= 1;
                coordinate[1] += 1;
                break;
            case 10:
                coordinate[0] -= 1;
                coordinate[1] -= 1;
                break;
            case 11:
                coordinate[0] += 1;
                coordinate[2] += 1;
                break;
            case 12:
                coordinate[0] += 1;
                coordinate[2] -= 1;
                break;
            case 13:
                coordinate[0] -= 1;
                coordinate[2] += 1;
                break;
            case 14:
                coordinate[0] -= 1;
                coordinate[2] -= 1;
                break;
            case 15:
                coordinate[1] += 1;
                coordinate[2] += 1;
                break;
            case 16:
                coordinate[1] += 1;
                coordinate[2] -= 1;
                break;
            case 17:
                coordinate[1] -= 1;
                coordinate[2] += 1;
                break;
            case 18:
                coordinate[1] -= 1;
                coordinate[2] -= 1;
                break;
        }
        return coordinate;
    }
}

class Node {
    int[] pre;
    int cost;
    int stepCost;
    int[] action;
    boolean visited = false;

    public void Node(int[] action) {
        this.action = action;
    }

    public void Node() {
        //
    }
}