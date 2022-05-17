public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        
        String pref = "";
        int smallest_length = 200;
        
        // finding smallest length
        for (int y = 0; y < strs.length; y++){
            if (strs[y].length() < smallest_length){
                smallest_length = strs[y].length();
            }
        }
    
        int i = 0;
        
        while (i < smallest_length){
            char common = strs[0].charAt(i);
            for (int x = 0; x < strs.length; x++){
                if (strs[x].charAt(i) != common){
                return pref;
            }
        }
        pref = pref + common;
        i++;
    
        }

        return pref;
        }
        
}