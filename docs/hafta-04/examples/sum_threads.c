/* Özgün, küçük öğretim örneği. Linux/Pthreads.
 * Derleme: cc -Wall -Wextra -Werror -pthread sum_threads.c -o sum_threads
 */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct job { int upper; long result; };
static void *sum(void *argument) {
    struct job *work = argument; /* main içindeki işin adresini al. */
    long total = 0;             /* Bu çağrıya ait yerel değişken. */
    for (int i = 1; i <= work->upper; ++i) total += i;
    work->result = total;      /* Ana thread join'den sonra okuyacak. */
    return NULL;
}
int main(void) {
    struct job work = { .upper = 5, .result = 0 };
    pthread_t worker;
    int rc = pthread_create(&worker, NULL, sum, &work);
    if (rc != 0) { fprintf(stderr, "create: %s\n", strerror(rc)); return EXIT_FAILURE; }
    rc = pthread_join(worker, NULL); /* İş tamamlanana kadar bekle. */
    if (rc != 0) { fprintf(stderr, "join: %s\n", strerror(rc)); return EXIT_FAILURE; }
    printf("Toplam: %ld\n", work.result);
    return EXIT_SUCCESS;
}
