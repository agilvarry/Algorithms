# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def rotate(matrix)
    m = transpose(matrix)
    reflect(m)
end

def transpose(matrix)
    l = matrix.length
    (0..l-1).each do |i|
        (i+1..l-1).each do |j|
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        end
    end
    matrix
end

def reflect(matrix)
    l = matrix.length
    (0..l-1).each do |i|
        (0..l/2).each do |j|
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        end
    end
    matrix
end