#include <stdio.h>
#include <stdlib.h>

#include "vdo.h"
#include "dpx.h"
#include "utl.h"
#include "cmd_parse.h"
#include "logging.h"


static int dpxRForceBe;
static int dpxRDatumOrder;
static int dpxRPadEnds;
static int dpxWPadEnds;
static int dpxWDatumOrder;
static int dpxWForcePacking;
static int dpxWByteSwap;
FILE  *fn_in;
FILE *fn_ppm;
void ppm_write_data();
pic_t* ip = NULL;
void main()
{
	int i, j;
	pic_t* ip = NULL;
	int rbSwap;
	char f[128], infname[128], bitsfname[128];
	sprintf(infname, "1.dpx");
	fn_ppm = fopen("1.ppm", "wb");
	dpxRPadEnds = 1;
	dpxRForceBe = 0;
	dpxRDatumOrder = 1;
	rbSwap = 1;



	dpx_read(infname, &ip, dpxRPadEnds, dpxRForceBe, dpxRDatumOrder, rbSwap);
	ppm_write_data();
}

void ppm_write_data()
{
	unsigned char ppm_header[17];
	int i, j, k;
	unsigned char rgb[3][3840][2400];
	for (k = 0; k < 3; k++)
	{
		for (i = 0; i < 2400; i++)
		{
			for (j = 0; j < 3840; j++)
			{
				rgb[k][j][i] = 0;
			}
		}
	}
	ppm_header[0] = 0x50;
	ppm_header[1] = 0x36;
	ppm_header[2] = 0x0a;
	ppm_header[3] = 0x33;
	ppm_header[4] = 0x38;
	ppm_header[5] = 0x34;
	ppm_header[6] = 0x30;
	ppm_header[7] = 0x20;
	ppm_header[8] = 0x32;
	ppm_header[9] = 0x31;
	ppm_header[10] = 0x36;
	ppm_header[11] = 0x30;
	ppm_header[12] = 0x0a;
	ppm_header[13] = 0x32;
	ppm_header[14] = 0x35;
	ppm_header[15] = 0x35;
	ppm_header[16] = 0x0a;
	for (i = 0; i < 17; i++)
	{
		fputc(ppm_header[i], fn_ppm);
	}
	for (i = 0; i < ip->h; i++)
	{
		for (j = 0; j < ip->w; j++)
		{
			rgb[0][j][i] = ip->data.rgb.r[i][j];
			rgb[1][j][i] = ip->data.rgb.g[i][j];
			rgb[2][j][i] = ip->data.rgb.b[i][j];
		}
	}
}