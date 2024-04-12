package com.autoaid.drools;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class Siniestro {
    private LocalDateTime fechaYHora;
    private String ubicacion;
    private String tipoAparcamiento;
    private String llamadaPolicia;
    private String matricula;
    private String numeroIncidenciaPolicial;
    private String testigo; // Puedes usar null para indicar la ausencia de testigos
    private String contactoTestigo;
    private String vehiculosPropiedadesInvolucrados;
    private int reincidenciaUltimoAnno;
    private int reincidencia3Anno;
    private int fraudes;
    private String tipoCobertura;
    private LocalDate inicioPoliza;
    private LocalDate finPoliza;
    private int edadConductor;
    private int anosCarnet;
    private double importePoliza;
    private String usoVehiculo;
    private int puntosCarnet;
    private String extrasPoliza;

    // Constructor
    public Siniestro() {}

    // Getters y setters
    public LocalDateTime getFechaYHora() {
        return fechaYHora;
    }

    public void setFechaYHora(LocalDateTime fechaYHora) {
        this.fechaYHora = fechaYHora;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

    public String getTipoAparcamiento() {
        return tipoAparcamiento;
    }

    public void setTipoAparcamiento(String tipoAparcamiento) {
        this.tipoAparcamiento = tipoAparcamiento;
    }

    public String getLlamadaPolicia() {
        return llamadaPolicia;
    }

    public void setLlamadaPolicia(String llamadaPolicia) {
        this.llamadaPolicia = llamadaPolicia;
    }

    public String getContactoTestigo() {
        return contactoTestigo;
    }

    public void setContactoTestigo(String contactoTestigo) {
        this.contactoTestigo = contactoTestigo;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getNumeroIncidenciaPolicial() {
        return numeroIncidenciaPolicial;
    }

    public void setNumeroIncidenciaPolicial(String numeroIncidenciaPolicial) {
        this.numeroIncidenciaPolicial = numeroIncidenciaPolicial;
    }

    public String getTestigo() {
        return testigo;
    }

    public void setTestigo(String testigo) {
        this.testigo = testigo;
    }

    public String getVehiculosPropiedadesInvolucrados() {
        return vehiculosPropiedadesInvolucrados;
    }

    public void setVehiculosPropiedadesInvolucrados(String vehiculosPropiedadesInvolucrados) {
        this.vehiculosPropiedadesInvolucrados = vehiculosPropiedadesInvolucrados;
    }

    public int getReincidenciaUltimoAnno() {
        return reincidenciaUltimoAnno;
    }

    public void setReincidenciaUltimoAnno(int reincidenciaUltimoAnno) {
        this.reincidenciaUltimoAnno = reincidenciaUltimoAnno;
    }

    public int getReincidencia3Anno() {
        return reincidencia3Anno;
    }

    public void setReincidencia3Anno(int reincidencia3Anno) {
        this.reincidencia3Anno = reincidencia3Anno;
    }

    public int getFraudes() {
        return fraudes;
    }

    public void setFraudes(int fraudes) {
        this.fraudes = fraudes;
    }
    public LocalDate getInicioPoliza() {
        return inicioPoliza;
    }
    
    public void setInicioPoliza(LocalDate inicioPoliza) {
        this.inicioPoliza = inicioPoliza;
    }
    
    public LocalDate getFinPoliza() {
        return finPoliza;
    }
    
    public void setFinPoliza(LocalDate finPoliza) {
        this.finPoliza = finPoliza;
    }
    
    public int getEdadConductor() {
        return edadConductor;
    }
    
    public void setEdadConductor(int edadConductor) {
        this.edadConductor = edadConductor;
    }
    
    public int getAnosCarnet() {
        return anosCarnet;
    }
    
    public void setAnosCarnet(int anosCarnet) {
        this.anosCarnet = anosCarnet;
    }
    
    public double getImportePoliza() {
        return importePoliza;
    }
    
    public void setImportePoliza(double importePoliza) {
        this.importePoliza = importePoliza;
    }
    
    public String getUsoVehiculo() {
        return usoVehiculo;
    }
    
    public void setUsoVehiculo(String usoVehiculo) {
        this.usoVehiculo = usoVehiculo;
    }

    public String getTipoCobertura() {
        return tipoCobertura;
    }
    
    public void setTipoCobertura(String tipoCobertura) {
        this.tipoCobertura = tipoCobertura;
    }
    
    public int getPuntosCarnet() {
        return puntosCarnet;
    }
    
    public void setPuntosCarnet(int puntosCarnet) {
        this.puntosCarnet = puntosCarnet;
    }
    
    public String getExtrasPoliza() {
        return extrasPoliza;
    }
    
    public void setExtrasPoliza(String extrasPoliza) {
        this.extrasPoliza = extrasPoliza;
    }
    
}

