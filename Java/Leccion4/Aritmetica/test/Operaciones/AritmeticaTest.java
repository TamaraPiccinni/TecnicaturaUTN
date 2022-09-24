/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Operaciones;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Usuario
 */
public class AritmeticaTest {
    
    public AritmeticaTest() {
    }
    
    @BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }

    /**
     * Test of sumarNumeros method, of class Aritmetica.
     */
    @Test
    public void testSumarNumeros() {
        System.out.println("sumarNumeros");
        Aritmetica instance = new Aritmetica();
        instance.sumarNumeros();
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of sumarConRetorno method, of class Aritmetica.
     */
    @Test
    public void testSumarConRetorno() {
        System.out.println("sumarConRetorno");
        Aritmetica instance = new Aritmetica();
        int expResult = 0;
        int result = instance.sumarConRetorno();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of sumarConArgumentos method, of class Aritmetica.
     */
    @Test
    public void testSumarConArgumentos() {
        System.out.println("sumarConArgumentos");
        int a = 0;
        int b = 0;
        Aritmetica instance = new Aritmetica();
        int expResult = 0;
        int result = instance.sumarConArgumentos(a, b);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
