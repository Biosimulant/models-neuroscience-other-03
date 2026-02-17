load test.txt
for row=1:3
for col=1:5
  if (row==1 && col==1)     % the first column is time
    continue
  end
  subplot(3,5,(row-1)*5+col)
  hold on
  plot(test(:,1),test(:,(row-1)*5+col))
  title(num2str((row-1)*5+col))
end
end
