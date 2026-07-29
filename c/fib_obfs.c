#include <stdlib.h>
#include <stdio.h>
#include <string.h>



                                                            void rs(char *d, char *s)
                                            { size_t l = strlen(s); for (size_t i = 0; i < l; i++)
                                          { d[i] = s[l - 1 - i]; } d[l] = '\0'; } void as(char *i1,
                                        char *i2, char *d) { int i = 0;  size_t s1l = strlen(i1); size_t
                                      s2l = strlen(i2); int c = 0; char *s1 = malloc((s1l + 1) * sizeof(
                                      char)); char *s2 = malloc( (s2l + 1) * sizeof(char));if(s2==NULL||
                                      s2==NULL) { printf("an error              occured when allocating");
                                      exit(1);}rs(s1, i1);rs(s2, i2);         while(i<s1l|| i<s2l||c==1)
                                        { int r=c;if (i<s1l){r+=            s1[i] - '0'; } if (i < s2l)
                                          {r+=s2[i]-'0';} if               (r > 9) { c = 1; r -= 10; }
                                                                          else{c= 0;}d[i]=r+'0';i++;}
                                                                        free(s1);free(s2);d[i] ='\0';
                                                                    char dc[strlen(d)+1];strcpy(
                                                                    dc,d);rs(d,dc);} int ct(char 
                                                                      *n) { int c = 0; for(size_t
                                                                       i=0; i< strlen(n); i++ ) {
                                        if(n[i]=='3'){c++;}}            return c;}int main(int argc,
                                      char *argv[]){if(argc!=2){        printf("USAGE: %s <num>\n",argv
                                    [0]); return 1;}int it=atoi(       argv[1])-2;int bf=0.25*it+2;char
                                    a[bf];char b[bf];char c[bf];int    tc=0;a[0]='0';a[1]='\0';b[0]='1';
                                    b[1]='\0';if(it>-2){printf("%s\n",a);}if(it> -1){printf("%s\n",b);}
                                      for(int i=0;i<it;i++){as(a,b,c);strcpy(a,b);strcpy(b,c);if(i<98)
                                      {printf("%s\n",b);}else if(i==98){printf("...\n");}tc+=ct(b);}
                                              printf("\n"); printf("There were %d threes\n",
                                                      tc); int du; int gu; return 0; }
