package com.autoaid.drools;

import org.kie.api.runtime.KieSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Collections;

@RestController
public class SiniestroController {
    @Autowired
    private KieSession kieSession;

    private final ObjectMapper mapper;

    public SiniestroController() {
        this.mapper = new ObjectMapper();
        // Registra el módulo para soportar LocalDateTime y otros tipos de Java 8
        this.mapper.registerModule(new JavaTimeModule());
    }

    @PostMapping("/procesar-siniestro")
    public ResponseEntity<Map<String, Object>> procesarSiniestro(@RequestBody String siniestroJson) {
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
            
            return ResponseEntity.ok(result);
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                 .body(Collections.singletonMap("error", "Error procesando el siniestro."));
        }
    }
}
