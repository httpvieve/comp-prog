call = float(input())
text = float(input())
call_charge = 0
text_charge = 0
fee = 25
cost = float(799.00 + fee)
print("Call minutes: " + str(call) + "\nText messages: " + str(text))
if call > 60 or text > 100:
  if call > 60:
    call_charge = float((call - 60) * 6.50)
  if text > 100:
    text_charge = float(text - 100)
  cost = cost + call_charge + text_charge
print("Excess minute charges: " + str("{:.2f}".format(call_charge)) + "\nExcess SMS charges: " + str("{:.2f}".format(text_charge)))
tax = float(0.05 * cost)
total = float(cost + tax)
print("911 fee: " + str("{:.2f}".format(fee)) +"\nTax: " + str("{:.2f}".format(tax)) + "\nTotal bill: " + str("{:.2f}".format(total)))


# #include <stdio.h>
# #include <string.h>
# #include <stdlib.h>

# int main()
# {
#     int size = 3;
#     char word[30];
    
#     char **word_list =  malloc(sizeof(word_list) * size);
    
#     printf("Enter %d Words\n",size);
    
#     for(int i =0; i<size; ++i){
    
#         scanf("%30s",word);
        
#         int word_size = strlen(word)+1;
        
#         word_list[i] = malloc(word_size);
        
#         strncpy(word_list[i],word,word_size);
#     }
    
#     printf("\nEntered words are\n");

#     for(int i=0; i<size; ++i){
#         printf("%s ",word_list[i]);
#     }
    
    
#     //resizing the capacity of the array
#     {
#         int resize;
#         printf("\nresize array size to: ");
#         scanf("%d",&resize);
        
#         if(size<resize){
#             for(int i=size-1; i>=resize; --i)
#                 free(word_list[i]);
#         }        
        
#         word_list = realloc(word_list, sizeof(word_list) * resize);
        
#         if(resize > size)
#             printf("Enter %d Words \n",resize-size);
        
#         for(int i =size; i<resize; ++i){
        
#             scanf("%30s",word);
            
#             int word_size = strlen(word)+1;
            
#             word_list[i] = malloc(word_size);
            
#             strncpy(word_list[i],word,word_size);
#         }
        
#         size = resize;
#     }
    
#     printf("Current words are\n");
#     for(int i=0; i<size; ++i){
#         printf("%s ",word_list[i]);
#     }
    
    
#     //Memory deallocation
#     for(int i=0; i<size; ++i){
#         free(word_list[i]);
#     }
    
#     free(word_list);
    
    
#     return 0;
# }