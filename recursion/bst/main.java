package recursion.bst;

import java.util.Arrays;
import java.util.Scanner;

public class main {
    static int size = 0;
    static int height = 0;
    static int sumOfWeight = 0;
    static int sumOfPathWeight = 0;
    static String ans = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            Node root = new Node();

            for (int i = 1; i < numbers[0] + 1; i++) {
                insert(root, numbers[i]);
                main.sumOfWeight += numbers[i];
            }
            main.size = numbers[0];

            size(root);

            height(root);

            sumOfWeight(root);

            maxPathWeight(root, 0);
            System.out.println(main.sumOfPathWeight);

            mirror(root);

            preOrder(root);
            System.out.println(main.ans.trim());
            main.ans = "";

            inOrder(root);
            System.out.println(main.ans.trim());
            main.ans = "";

            postOrder(root);
            System.out.println(main.ans.trim());
            main.ans = "";

            destruct(root);

            if (root == null || root.getData() == -1) {
                System.out.println(0);
            } else {
                System.out.println(1);
            }

            size = 0;
            height = 0;
            sumOfWeight = 0;
            sumOfPathWeight = 0;

            loop--;
        }
    }

    private static void maxPathWeight(Node now, int sum) {
        if (now == null || now.getData() == -1) {
            if (sum > main.sumOfPathWeight) {
                main.sumOfPathWeight = sum;
            }
        } else {
            sum += now.getData();
            maxPathWeight(now.getLeft(), sum);
            maxPathWeight(now.getRight(), sum);
        }
    }

    private static void mirror(Node now) {
        if (now == null) {
            return;
        }

        mirror(now.getLeft());
        mirror(now.getRight());

        swap(now);
    }

    private static void swap(Node now) {
        if (now == null) {
            return;
        }

        Node temp = now.getLeft();
        now.setLeft(now.getRight());
        now.setRight(temp);
    }

    private static void destruct(Node root) {
        root.setData(-1);
        root.setLeft(null);
        root.setRight(null);
    }

    private static void sumOfWeight(Node root) {
        System.out.println(main.sumOfWeight);
    }

    private static void height(Node root) {
        System.out.println(main.height);
    }

    private static void size(Node now) {
        System.out.println(main.size);
    }

    private static void postOrder(Node now) {
        if (now == null || now.getData() == -1) {
            return;
        } else {
            postOrder(now.getLeft());
            postOrder(now.getRight());
            ans += now.getData() + " ";
        }
    }

    private static void inOrder(Node now) {
        if (now == null || now.getData() == -1) {
            return;
        } else {
            inOrder(now.getLeft());
            ans += now.getData() + " ";
            inOrder(now.getRight());
        }
    }

    private static void preOrder(Node now) {
        if (now == null || now.getData() == -1) {
            return;
        } else {
            ans += now.getData() + " ";
            preOrder(now.getLeft());
            preOrder(now.getRight());
        }
    }

    private static void insert(Node now, int number) {
        Node parent = now;
        String direction = "";
        int heightCounter = 0;

        if ((now == null || now.getData() == -1) && now.getLeft() == null && now.getRight() == null) {
            now.setData(number);
            return;
        }

        while (now != null) {
            if (now.getData() > number) {
                parent = now;
                direction = "left";
                now = now.getLeft();
            } else {
                parent = now;
                direction = "right";
                now = now.getRight();
            }
            heightCounter++;
        }

        if (direction.equals("left")) {
            parent.setLeft(new Node(number));
        } else {
            parent.setRight(new Node(number));
        }

        if (main.height < heightCounter) {
            main.height = heightCounter;
        }
    }


    static class Node {
        private int data;
        private Node left;
        private Node right;

        public Node() {
            this.data = -1;
        }

        public Node(int data) {
            this.data = data;
        }

        int getData() {
            return data;
        }

        void setData(int data) {
            this.data = data;
        }

        public Node getLeft() {
            return left;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public Node getRight() {
            return right;
        }

        public void setRight(Node right) {
            this.right = right;
        }
    }
}
