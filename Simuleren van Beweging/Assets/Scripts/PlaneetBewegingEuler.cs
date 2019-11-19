using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneetBewegingEuler : MonoBehaviour
{
    public float h;
    public float earthMass;
    public float gConst;
    public GameObject other;
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;

    private Rigidbody rb;

    void Start()
    {
        // earthMass = 5.97e24f;
        // gConst = 6.67e-11f;
        rb = GetComponent<Rigidbody>();

    }

    Vector3 acceleration(Vector3 moon)
    {
        return gConst * earthMass / (float)Math.Pow((-moon).magnitude, 3) * (-moon);
    }

    void FixedUpdate()
    {
        Acceleration = acceleration(transform.position);
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;

        // transform.position += Time.deltaTime * Time.deltaTime * ;
    }
}
