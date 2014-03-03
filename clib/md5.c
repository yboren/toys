#include <openssl/md5.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

/* calculate the md5sum of the first bytes of the in buf
 * result will be stored in out buf
 * return 0 for success, othervise for fail
 */
int md5_buf(void *out, void *in, size_t bytes)
{
	int ret = 0, i = 0;
	MD5_CTX md5_ctx;

	if( (out == NULL) || (in == NULL) )
		return -1;

	if(MD5_Init(&md5_ctx) == 0)
		return -2;

	if(MD5_Update(&md5_ctx, in, bytes) == 0)
		return -4;

	if(MD5_Final(out, &md5_ctx) == 0)
		return -5;

	return 0;
}

#define print_md5sum(md5_result) do {\
	int i = 0; \
	printf("%s:", #md5_result); \
	for(i = 0; i < MD5_DIGEST_LENGTH; i++) \
	printf("%02x", (unsigned char)md5_result[i]); \
	printf("\n"); \
}while(0)
