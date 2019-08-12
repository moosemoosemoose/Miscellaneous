package matrixBin;
import java.util.*; 
import java.io.*;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class matrixBin
{
	private static final String targetFile = "matrix0600x0600.bin";
	private static final String targetFile2 = "m0016x0016.bin";
	private static final String targetFile3 = "matrix04x04.bin";

	public static void printToBIN(int[][] cityMatrix2, int numCities) throws IOException 
	{	   
		OutputStream out = null;
		
		try
		{
		     out = new FileOutputStream(targetFile3);
		     byte[] totalBytes = new byte[numCities*numCities];
		     
		     int i = 0;
		     
		     for(int x=0; x < numCities; x++)
			 {
					for(int y=0; y < numCities; y++)
					{
						totalBytes[i] = (byte)(cityMatrix2[x][y]);
						i++;
					}		
			 }
		     
		     out.write(totalBytes);
		}
		    
		finally
		{
		    if(out !=null)
		        out.close();
		}	    
	}
	
	public static void readFromBIN(int[][] cityMatrix, int numCities) throws IOException
	{
		int i = 0;
		byte[] allBytes = new byte[numCities*numCities];
		InputStream fileIS = new FileInputStream(targetFile);
		fileIS.read(allBytes);
		
		for(int x = 0; x < numCities; x++)
		{
	    	for(int y = 0; y < numCities; y++)
	    	{
	    		cityMatrix[x][y] = allBytes[i];
	    		i++; 
	    		//System.out.println();
	    	}
	    }    
		fileIS.close();
	}
	
	public static void readFromBIN2(int[][] cityMatrix2, int numCities) throws IOException
	{
		byte[] allBytes = new byte[numCities*numCities*4];
		
		InputStream fileIS = new FileInputStream(targetFile);
		fileIS.read(allBytes);
		ByteBuffer buf = ByteBuffer.wrap(allBytes).order(ByteOrder.LITTLE_ENDIAN);
		int temp = 0;
		String tempS = "";
		
		for(int x = 0; x < numCities; x++)
		{
	    	for(int y = 0; y < numCities; y++)
	    	{
	    		
	    		temp = buf.getInt(); 
	    		
	    		tempS = Integer.toString(temp);
	    		
	    		System.out.print(tempS + " ");
	    		
	    	}
	    } 

		fileIS.close();
	}
	public static byte[] hexStringToByteArray(String hex) {
	    int l = hex.length();
	    byte[] data = new byte[l/2];
	    for (int i = 0; i < l; i += 2) {
	        data[i/2] = (byte) ((Character.digit(hex.charAt(i), 16) << 4)
	                             + Character.digit(hex.charAt(i+1), 16));
	    }
	    return data;
	}
	
	public static void makeMatrix(int cityMatrix[][], int numCities)
	{
		int randNum = 0;
		
		for(int x = 0; x < numCities; x++)
		{
			for(int y=0; y < numCities; y++)
			{
				if(x!=y)
				{
					randNum = (int)(Math.random()*100+1);
					cityMatrix[x][y] = randNum;
				}
				
				else
				{
					cityMatrix[x][y] = 0;
			  	}
			}
		}
	}
	
	public static void printMatrix(int[][] cityMatrix, int numCities)
	{		
		for(int x=0; x<numCities; x++)
		{
			for(int y=0; y<numCities; y++)
			{
				System.out.printf("%d ", cityMatrix[x][y]);
			}
			
			System.out.println();
		}
		
	}
	
	public static void printMatrix2(double[][] cityMatrix2, int numCities)
	{		
		for(int x=0; x<numCities; x++)
		{
			for(int y=0; y<numCities; y++)
			{
				System.out.printf("%.6f ", cityMatrix2[x][y]);
			}
			
			System.out.println();
		}
	}
	
	public static List<Integer> pathShuffle3Opt(List<Integer> path)
	{
		int randNum, randNum2, randNum3 = 0;
		randNum = (int)(Math.random()*599+0);
		randNum2 = (int)(Math.random()*599+0);
		randNum3 = (int)(Math.random()*599+0);
		
		Collections.shuffle(path);
		Collections.swap(path, randNum, randNum2); 
		Collections.swap(path, randNum, randNum3);
		
		return path;
	}
		
	public static List<Integer> path2Opt(List <Integer> path)
	{
		int randNum, randNum2 = 0;
		randNum = (int)(Math.random()*599+0);
		randNum2 = (int)(Math.random()*599+0);
		Collections.swap(path, randNum, randNum2); 
		
		return path;
	}

	public static List<Integer> path3Opt(List <Integer> path)
	{
		int randNum, randNum2, randNum3 = 0;
		randNum = (int)(Math.random()*599+0);
		randNum2 = (int)(Math.random()*599+0);
		randNum3 = (int)(Math.random()*599+0);
		Collections.swap(path, randNum, randNum2); 
		Collections.swap(path, randNum, randNum3);
		
		return path;
	}
	
	public static int calcDistance(List<Integer> pathCreated, int[][] cityMatrix, int bestDistance)
	{
		int pathDistance = 0;
		
		for(int i=0; i < pathCreated.size(); i++)
		{
			if(i < pathCreated.size() - 1)
			{
				pathDistance += cityMatrix[pathCreated.get(i)-1][pathCreated.get(i+1)-1];
				
				if(pathDistance > bestDistance)
				{
					break;
				}
			}
			
			else
			{
				pathDistance += cityMatrix[pathCreated.get(i)-1][pathCreated.get(0)-1];
			}
		}
		
		//System.out.println("");
		//System.out.print("Path: \t" + pathCreated);
		//System.out.println("");
		
		return pathDistance;
	}
	
	public static double calcDistance2(List<Integer> pathCreated, double[][] cityMatrix2, int bestDistance)
	{
		double pathDistance = 0;
		
		for(int i=0; i < pathCreated.size(); i++)
		{
			if(i < pathCreated.size() - 1)
			{
				pathDistance += cityMatrix2[pathCreated.get(i)-1][pathCreated.get(i+1)-1];
				
				if(pathDistance > bestDistance)
				{
					break;
				}
			}
			
			else
			{
				pathDistance += cityMatrix2[pathCreated.get(i)-1][pathCreated.get(0)-1];
			}
		}
		
		//System.out.println("");
		//System.out.print("Path: \t" + pathCreated);
		//System.out.println("");
		
		return pathDistance;
	}
		
	public static void main (String[] args) throws FileNotFoundException
	{
		int numCities = 600;
		int[][] cityMatrix = new int[numCities][numCities];
		int pathDistance = 0;
		int bestDistance = Integer.MAX_VALUE;
		//double bestDistance2 = Double.MAX_VALUE;	
		//double pathDistance2 = 0;
		//double[][] cityMatrix2 = new double[numCities][numCities];
		List<Integer> winner = new ArrayList<Integer>();
		List<Integer> pathCreated = new ArrayList<Integer>();
		long time = 0;
		long end = 0;
		//makeMatrix(cityMatrix, numCities);
		
		try 
		{			
			readFromBIN(cityMatrix, numCities);
			//readFromBIN2(cityMatrix, numCities);
			System.out.println("Read File.");
		}
		
		catch (Exception ioE) 
		{
			System.out.println("Could Not Read File.");
		} 
		
		
		//printMatrix(cityMatrix, numCities);
		//printMatrix2(cityMatrix2, numCities);
		
		time = System.currentTimeMillis();
		end = time+60000;
		
		while(System.currentTimeMillis() < end)
		{
			List<Integer> bestPath = new ArrayList<Integer>();
			List<Integer> path = new ArrayList<Integer>();
			
			for(int i=1; i<numCities+1; i++)
			{
				path.add(i);
			}
			
			pathCreated = pathShuffle3Opt(path);
			pathDistance = calcDistance(pathCreated, cityMatrix, bestDistance);
			//pathDistance2 = calcDistance2(pathCreated, cityMatrix2, bestDistance);
			
			if(pathDistance<bestDistance)
			{
				bestDistance = pathDistance;
				bestPath = pathCreated;
				winner = bestPath;
			}
			
			/*if(pathDistance2<bestDistance2)
			{
				bestDistance2 = pathDistance2;
				bestPath = path;
				winner = bestPath;
			}*/
	
		}
		
		System.out.println("The best path is: " + winner);
		System.out.println("Total distance of the best path is: " + bestDistance);
		//System.out.printf("Total distance of the best path is: %.6f\n" , bestDistance2);
		
		/*try 
		{
			printToBIN(cityMatrix, numCities);
			System.out.println("It is written.");
		}
		
		catch (Exception ioE) 
		{
			System.out.println("Nope");
		}*/
	}
}