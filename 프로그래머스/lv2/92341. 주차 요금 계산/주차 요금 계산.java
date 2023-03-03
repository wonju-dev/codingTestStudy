import java.time.LocalTime;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {

    static int basicMinute;
    static int basicFee;
    static int plusMinute;
    static int plusFee;

    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};

        basicMinute = fees[0];
        basicFee = fees[1];
        plusMinute = fees[2];
        plusFee = fees[3];

        Map<String, Info> parkingRecords = new HashMap<>();
        Map<String, Integer> accum = new HashMap<>();
        getInfos(records).stream().forEach(info -> {
            if (info.status == Status.IN) {
                parkingRecords.put(info.number, info);
            } else {
                Info parkInInfo = parkingRecords.get(info.number);
                if (accum.get(info.number) != null) {
                    accum.put(info.number, accum.get(info.number) + toMinute(info) - toMinute(parkInInfo));
                } else {
                    accum.put(info.number, toMinute(info) - toMinute(parkInInfo));
                }
                parkingRecords.remove(info.number);
            }
        });
        parkingRecords.keySet().stream().forEach(number -> {
            Info info = parkingRecords.get(number);
            if (accum.get(info.number) != null) {
                accum.put(info.number, accum.get(info.number) + toMinute(new Info("23:59 " + info.number + " OUT")) - toMinute(info) );
            } else {
                accum.put(info.number, toMinute(new Info("23:59 " + info.number + " OUT")) - toMinute(info));
            }
        });
        return accum.keySet().stream().sorted(String::compareTo).map(n -> calculatePrice(accum.get(n))).mapToInt(Integer::valueOf).toArray();
    }

    private Integer calculatePrice(int minute) {
        if (minute <= basicMinute) {
            return basicFee;
        }
        Integer overMinute = minute - basicMinute;
        int mock = overMinute / plusMinute;
        int namuzi = overMinute % plusMinute;
        if (namuzi != 0) {
            return basicFee + plusFee * (mock + 1);
        } else {
            return basicFee + plusFee * mock;
        }
    }

    private Integer toMinute(Info info) {
        return info.time.getHour() * 60 + info.time.getMinute();
    }

    private List<Info> getInfos(String[] records) {
        return Arrays.stream(records).map(s -> new Info(s)).collect(Collectors.toList());
    }

    private class Info {
        LocalTime time;
        String number;
        Status status;

        public Info(String data) {
            String[] chunks = data.split(" ");
            String[] time = chunks[0].split(":");
            this.time = LocalTime.of(Integer.parseInt(time[0]), Integer.parseInt(time[1]));
            this.number = chunks[1];
            this.status = chunks[2].equals("IN") ? Status.IN : Status.OUT;
        }
    }

    private enum Status {
        IN,
        OUT
    }
}