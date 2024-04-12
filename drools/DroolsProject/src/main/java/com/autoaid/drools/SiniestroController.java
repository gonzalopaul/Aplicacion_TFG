package com.autoaid.drools;

import org.kie.api.runtime.KieSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import org.springframework.http.HttpStatus;

import java.util.Map;



@RestController
public class SiniestroController {
    @Autowired
    private KieSession kieSession;

    @PostMapping("/procesar-siniestro")
public ResponseEntity<Map<String, Object>> procesarSiniestro(@RequestBody String siniestroJson) {
    ObjectMapper mapper = new ObjectMapper();
    try {
        Siniestro siniestro = mapper.readValue(siniestroJson, Siniestro.class);
        List<String> respuestas = new ArrayList<>();
        List<String> recomendaciones = new ArrayList<>();
        
        // Establecer las listas como globales en la sesión de Kie
        kieSession.setGlobal("respuestas", respuestas);
        kieSession.setGlobal("recomendaciones", recomendaciones);
        
        kieSession.insert(siniestro);
        kieSession.fireAllRules();
        
        Map<String, Object> result = new HashMap<>();
        result.put("respuestas", respuestas);
        result.put("recomendaciones", recomendaciones);
        
        return new ResponseEntity<>(result, HttpStatus.OK);
    } catch (Exception e) {
        e.printStackTrace();
        return new ResponseEntity<>(Collections.singletonMap("error", "Error procesando el siniestro."),
                                    HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
}
