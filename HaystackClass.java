class HaystackClass {
    public int strStr(String haystack, String needle) {
// account for needle being an empty string
if (needle.length() == 0){
    return 0;
}

int index = -1;
int needle_progress = 0;
int haystack_progress = 0;

while (haystack_progress < haystack.length() && needle_progress < needle.length()){
    if (haystack.charAt(haystack_progress) == needle.charAt(needle_progress)){
        index = haystack_progress;
        needle_progress++;
    }
    else if (needle_progress != 0){
        if (haystack.charAt(haystack_progress) == needle.charAt(0)){
            index = haystack_progress;
            needle_progress = 1;
        }
    }
    else {
        index = -1;
        needle_progress = 0;
    }
    haystack_progress++;
}

return index;
    }
}