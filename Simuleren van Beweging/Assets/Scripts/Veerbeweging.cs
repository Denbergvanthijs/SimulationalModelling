using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Veerbeweging : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;

    public int mass;
    public int veerConst;

    void FixedUpdate()
    {
        // F = -c * u
        Force = -veerConst * transform.position - 1 * Velocity;
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
