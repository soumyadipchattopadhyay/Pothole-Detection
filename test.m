 
  img = imread('C:\Users\chatt\OneDrive\Desktop\potholes4.jpg'); %garbbing an image
  B = imresize(img, [400 300]); %resizing it
  G = rgb2gray(B);   %converting it into gray
  BW = edge(G,'canny',0.6); %finding the edges
  se = ones(30,30);
  IM2 = imdilate(BW,se); %dilsting the image
  
  
  subplot(1,3,1); %plotting orignal resized image
  imshow(B);
  title('Resized orignal image');
  
  subplot(1,3,2);  %plotting edge detected image
  imshow(BW);
  title('Edge detection');
  
  subplot(1,3,3);  %plotting dialated image
  imshow(IM2);
  title('Dialated image');
  
  
  L= find(IM2==1);  %keeping all the '1s' in an array
  p = numel(L);  % calculate number of white/'1s'  pixels 
  
  if( p > 30000 ) %checking the condition
   
   disp(p); %displaying number of white pixel
   disp('pothole road');
   f = msgbox('Pothole Ahead');
      
  else
    
      disp( p);
      disp('clear road ahead');
     
     
  end
  