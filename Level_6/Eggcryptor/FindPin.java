import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.io.File.*;
import java.nio.file.*;

public class FindPin {
    private static final String EGG = "V1cwd05XUXhjRkpRVkRBOQ==";

    public static byte[] decrypt(String pin, String enc64) throws Exception {
        byte[] salt = new byte[8];
        for (int i = 0; i < 8; i++) {
            salt[i] = (byte) i;
        }
        SecretKeySpec key = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(new PBEKeySpec(pin.toCharArray(), salt, 10000, 128)).getEncoded(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(2, key);
        return cipher.doFinal(Base64.getDecoder().decode(enc64));
    }

    public static void main(String[] args) 
    {
        byte[] b;
        byte[] b2 = null;
        byte[] d = null;
        Path path = null;

        try {
            path = Paths.get("raw.raw");
            b2 = Files.readAllBytes(path);
            b = b2;
        } catch (Exception e) {
            b = b2;
        }

        final String r = new String(b);        
        String Pin;
        boolean found = false;
        char letter = 'a';
        int num = 0; 

        while (!found && letter < '{') {
            Pin = letter + String.format("%04d", num);

            try {
                d = decrypt(Pin, r);
            } catch (Exception e) {
            }

            if (d != null && d[0] == -119) {
               path = Paths.get("Pin_" + Pin + ".png");
               try {
                   Files.write(path, d);
               } catch (Exception e) {
               }
               System.out.println("File Pin_" + Pin + ".png created");
               found = true;
            } 
            num++;
                
            if (num == 10000) {
               num = 0;
               letter += 1;
            }
        }
    }
}