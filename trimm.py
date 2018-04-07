from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
import argparse


def trimmer(record,lencrop_l,lencrop_r,win,file):
    new_record = record[lencrop_l:len(str(record.seq))-lencrop_r]
    SeqIO.write(new_record, file, 'fastq')
    annot_rec = record.letter_annotations['phred_quality']
    q=0
    for i in range(0,len(annot_rec)-win,win):
        for j in range(i,i+win):
            if j <30:
                q+=1
                start=i
            else:
                continue
    if q > 0:
        new_record = new_record[:i] + new_record[i+win:]
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='my_personal_trimmomatic')
    parser.add_argument("-cl", "--crop_left", type = int, help='number of nucleotides to crop from left', default = 10)
    parser.add_argument("-cr", "--crop_right", type=int, help='number of nucleotides to crop from right', default = 5)
    parser.add_argument("-i", "--input", type=str, help='path to input file')
    parser.add_argument("-w", "--window", type=int, help='length of quality window', default = 10)
    parser.add_argument("-q","--quality",type=int, help='edge of quality score', default = 30)



    args=parser.parse_args()
    crop_length_left = args.crop_left
    crop_length_right = args.crop_right
    datafile = args.input
    window = args.window
    edge = args.quality
datafile=input()
#crop_length_left = 10
#crop_length_right = 5
#window = 10
#edge = 30
with open (datafile,'r') as data:
    with open(datafile + '_output', 'w') as out:
        for record in SeqIO.parse(data,'fastq'):
            trimmer(record, crop_length_left, crop_length_right, window, out)




