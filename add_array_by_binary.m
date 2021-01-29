function [array_size, matlab_time, m, glocal_count] = add_array_by_binary (file_path,row_number_count,col_number_count)


tic

global count

count = count + 1;

# A, B is the row and column number of input matrix
fid=fopen(file_path,'rb');
    if(fid>0)
        [data_array,data_count]=fread(fid,[row_number_count,col_number_count],'float64');
    end
fclose(fid);

m = sum(sum(data_array));

array_size = whos('data_array').bytes ./ 1024 ./ 1024;

matlab_time = toc;

end
