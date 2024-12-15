package corejava.core;

import java.util.HashMap;
import java.util.Map;

final class Immutable {
    private final String name;
    private final int regNo;
    private final Map<String, String> metadata;

    public Immutable(String name,int regNo, Map<String,String> metadata){
        this.name = name;
        this.regNo = regNo;
        Map<String, String> tempMap = new HashMap<>();
        for (Map.Entry<String, String> iterable_element : metadata.entrySet()) {
            tempMap.put(iterable_element.getKey(), iterable_element.getValue());
        }
        this.metadata = tempMap;

    }
    public String getName(){
        return this.name;
    }
    public int getNo(){
        return this.regNo;
    }

    public Map<String, String> getMetadata(){
        Map<String, String> tempMap = new HashMap<>();
        for (Map.Entry<String, String> iterable_element : this.metadata.entrySet()) {
            tempMap.put(iterable_element.getKey(),iterable_element.getValue());
        }
        return tempMap;
    }

}
