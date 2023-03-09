import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[][] r) {
        List<Route> routes = Arrays.stream(r).map(ro -> new Route(ro[0], ro[1])).sorted((r1, r2) -> r1.from - r2.from).collect(Collectors.toList());

        if (routes.size() == 1) {
            return 1;
        }

        int count = 1;
        Route standard = routes.get(0);

        for (int i = 1; i < routes.size(); i++) {
            Route route = routes.get(i);
            if (!standard.include(route)) {
                standard = route;
                count++;
            } else {
                standard = new Route(Math.max(standard.from, route.from), Math.min(standard.to, route.to));
            }
        }

        return count;
    }

    private class Route {
        int from;
        int to;

        public Route(int from, int to) {
            this.from = from;
            this.to = to;
        }

        public boolean include(Route route) {
            return this.from <= route.from && route.from <= this.to;
        }
    }
}