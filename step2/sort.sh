(head -n 1 T_values_EPD.txt && tail -n +2 T_values_EPD.txt | sort -t , -k 2 -g -r) > EPD_sort.txt;
mv EPD_sort.txt T_values_EPD.txt;
(head -n 1 T_values_JPA.txt && tail -n +2 T_values_JPA.txt | sort -t , -k 2 -g -r) > JPA_sort.txt;
mv JPA_sort.txt T_values_JPA.txt;
(head -n 1 T_values_MED.txt && tail -n +2 T_values_MED.txt | sort -t , -k 2 -g -r) > MED_sort.txt;
mv MED_sort.txt T_values_MED.txt;
(head -n 1 T_values_MGL.txt && tail -n +2 T_values_MGL.txt | sort -t , -k 2 -g -r) > MGL_sort.txt;
mv MGL_sort.txt T_values_MGL.txt;
(head -n 1 T_values_RHB.txt && tail -n +2 T_values_RHB.txt | sort -t , -k 2 -g -r) > RHB_sort.txt;
mv RHB_sort.txt T_values_RHB.txt;

